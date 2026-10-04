import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    valid_norms = {'l1', 'l2', 'linf', 'frobenius'}
    if norm_type not in valid_norms:
        raise ValueError(f"Invalid norm_type '{norm_type}'. Must be one of {valid_norms}")

    # Frobenius norm strict matrix validation
    if norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError("The 'frobenius' norm is only defined for 2D matrices.")
        return float(np.linalg.norm(arr, ord='fro'))

    # Entrywise norms: treat 1D or 2D input as a flat array of numbers
    if norm_type == 'l1':
        return float(np.sum(np.abs(arr)))
    elif norm_type == 'l2':
        return float(np.sqrt(np.sum(np.square(arr))))
    elif norm_type == 'linf':
        return float(np.max(np.abs(arr)))
