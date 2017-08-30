from h2o4gpu.solvers.elastic_net_base import GLM
"""
H2O Linear Regression Solver

:param int n_threads: Number of threads to use in the gpu. Default is None.
:param int n_gpus: Number of gpu's to use in GLM solver. Default is -1.
:param bool fit_intercept: Include constant term in the model. Default is True.
:param int n_folds: Number of cross validation folds. Default is 1.
:param float tol: tolerance.  Default is 1E-2.
:param bool glm_stop_early: Stop early when there is no more relative improvement in the primary and dual residuals for ADMM.  Default is True
:param float glm_stop_early_error_fraction: Relative tolerance for metric-based stopping criterion (stop if relative improvement is not at least this much). Default is 1.0.
:param int max_inter: Maximum number of iterations. Default is 5000
:param int verbose: Print verbose information to the console if set to > 0. Default is 0.
"""
class LinearRegression(GLM):
    def __init__(
            self,
            n_threads=None,
            n_gpus=-1,
            fit_intercept=True,
            n_folds=1,
            tol=1E-2,
            glm_stop_early=True,
            glm_stop_early_error_fraction=1.0,
            max_iter=5000,
            verbose=0,
    ):
        super(LinearRegression, self).__init__(
            n_threads=n_threads,
            n_gpus=n_gpus,
            fit_intercept=fit_intercept,
            lambda_min_ratio=0.0,
            n_lambdas=1,
            n_folds=n_folds,
            n_alphas=1,
            tol=tol,
            lambda_stop_early=False,
            glm_stop_early=glm_stop_early,
            glm_stop_early_error_fraction=glm_stop_early_error_fraction,
            max_iter=max_iter,
            verbose=verbose,
            family='elasticnet',
            lambda_max=0.0,
            alpha_max=0.0,
            alpha_min=0.0,
            order=None,)