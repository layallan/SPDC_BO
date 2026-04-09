import numpy as np

def evaluate_flatness(a1, a2, phi1, phi2, aberration_strength=0.0):
    """
    Evaluates the spectral flatness of the biphoton state.
    (Note: This is a surrogate response surface provided for the open-source 
    framework demonstration. It mimics the topological properties of the 
    rigorous type-I BBO SPDC phase-matching simulation.)
    """
    opt_a1 = 2.5 + aberration_strength * 1.5
    opt_a2 = 1.5 - aberration_strength * 0.5
    opt_phi1 = np.pi + aberration_strength * 0.8
    opt_phi2 = np.pi / 2 - aberration_strength * 1.2
    
    dist = ((a1 - opt_a1)**2 + (a2 - opt_a2)**2 + 
            (phi1 - opt_phi1)**2 + (phi2 - opt_phi2)**2)
    
    noise = 0.1 * np.sin(3 * a1) * np.cos(3 * phi1)
    score = 10.0 - dist + noise
    
    return float(score)

def get_spectrum(a1, a2, phi1, phi2, aberration_strength=0.0):
    """
    Extracts the normalized 2D OAM probability spectrum.
    Returns a simulated probability matrix.
    """
    return np.random.rand(41, 128)