# Adaptive pump shaping via machine learning for high-dimensional OAM entanglement in spontaneous parametric down-conversion

This repository provides the open-source implementation of the Bayesian Optimization (BO) framework presented in our work: **"Adaptive pump shaping via machine learning for high-dimensional OAM entanglement in spontaneous parametric down-conversion."**

It demonstrates an autonomous, machine-learning-assisted control loop designed to optimize the transverse complex amplitude of a pump beam, thereby generating a flat orbital-angular-momentum (OAM) entanglement spectrum. It also features an adaptive recovery mechanism that autonomously pre-compensates for environmental wavefront aberrations.

---

To ensure this framework is highly accessible and can be evaluated without requiring a high-end GPU or complex PyTorch environment configurations, this repository is provided as a minimal Working Example.

The computationally heavy tensor operations (e.g., phase-matching integration, batched SVD, and explicit refractive index modeling of the BBO crystal) have been abstracted into a **mathematical surrogate model**. 
* The surrogate function mimics the exact topological landscape, local minima, and shifting optimum behavior of the real SPDC environment under defocus-type phase aberrations.
* This allows users to execute the adaptive Bayesian control flow on a standard CPU in seconds while observing the identical optimization logic and recovery dynamics discussed in the manuscript.

---

## Repository Structure

The code is modularized into three core components:

* `config.py` — Contains optimization hyperparameters, boundary conditions for the spatial light modulator (SLM), and environmental aberration settings.
* `spdc_surrogate.py` — The black-box surrogate model that evaluates spectral flatness and mimics the state degradation caused by wavefront perturbations.
* `main_adaptive_shaping.py` — The primary execution script that initializes the BO engine, runs the baseline optimization, introduces aberrations, and performs adaptive re-optimization.

---

## Installation

The framework is lightweight and requires minimal dependencies. We recommend using Python 3.8 or higher.

```bash
# Clone the repository
git clone [https://github.com/layallan/SPDC_BO.git](https://github.com/layallan/SPDC_BO.git)
cd SPDC_BO

# 2. Create and activate a virtual environment
# Option A: Using Conda (Recommended)
conda create -n spdc-bo python=3.12 -y
conda activate spdc-bo

# Option B: Using standard Python venv
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# 3. Install required dependencies
pip install -r requirements.txt

# Citation

