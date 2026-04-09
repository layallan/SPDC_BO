import time
from bayes_opt import BayesianOptimization

# Import local modules
from config import PBOUNDS, ABERRATION_ENV, BO_INIT_POINTS, BO_N_ITER_IDEAL, BO_N_ITER_COMP
from spdc_surrogate import evaluate_flatness, get_spectrum

def run_optimization_loop(aberration, n_iter, random_state):
    """
    Executes the Bayesian Optimization target function.
    """
    optimizer = BayesianOptimization(
        f=lambda a1, a2, phi1, phi2: evaluate_flatness(a1, a2, phi1, phi2, aberration_strength=aberration),
        pbounds=PBOUNDS,
        random_state=random_state,
        verbose=2 
    )
    
    start_time = time.time()
    optimizer.maximize(init_points=BO_INIT_POINTS, n_iter=n_iter)
    elapsed = time.time() - start_time
    
    return optimizer.max, elapsed

if __name__ == "__main__":
    print("1. Initializing Ideal Pump Optimization")
    print("====================================================")
    res_ideal, time_ideal = run_optimization_loop(aberration=0.0, n_iter=BO_N_ITER_IDEAL, random_state=42)
    bp_ideal = res_ideal['params']
    
    print(f"\nOptimization completed in {time_ideal:.2f} sec.")
    print(f"Optimized Parameters: {bp_ideal}")
    print(f"Baseline Score: {res_ideal['target']:.4f}\n")

    print(f"Simulating Environmental Aberration (\u03b1 = {ABERRATION_ENV})")
    print("====================================================")
    score_degraded = evaluate_flatness(bp_ideal['a1'], bp_ideal['a2'], bp_ideal['phi1'], bp_ideal['phi2'], aberration_strength=ABERRATION_ENV)
    print(f"System degraded. Score without compensation: {score_degraded:.4f}\n")

    print("Re-optimization")
    print("====================================================")
    res_comp, time_comp = run_optimization_loop(aberration=ABERRATION_ENV, n_iter=BO_N_ITER_COMP, random_state=100)
    bp_comp = res_comp['params']
    
    print(f"\nAdaptive recovery completed in {time_comp:.2f} sec.")
    print(f"Compensated Parameters: {bp_comp}")
    print(f"Recovered Score: {res_comp['target']:.4f}")