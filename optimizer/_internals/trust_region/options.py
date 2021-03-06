from typing import Literal, Optional, Union


class Trust_Region_Options:
    border_abstol: float = 1e-10
    tol_step: float = 1.0e-10
    tol_grad: float = 1.0e-6
    abstol_fval: Optional[float] = None
    max_stall_iter: Optional[int] = None
    init_delta: float = 1.0
    max_iter: int
    check_rel: float = 1.0e-2
    check_abs: Optional[float] = None
    check_iter: Optional[int] = None  # 0表示只在最优化开始前进行一次梯度检查，-1表示完全关闭检查，默认的None表示始终进行检查
    shaking: Union[Literal["x.shape[0]"], int] = "x.shape[0]"
    display: bool = True

    def __init__(self, *, max_iter: int) -> None:
        self.max_iter = max_iter
