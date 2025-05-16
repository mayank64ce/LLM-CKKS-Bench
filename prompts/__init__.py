from .task_add_prompt import task_add
from .task_mult_prompt import task_mult
from .task_inner_prompt import task_inner
from .task_matmul_prompt import task_matmul
from .task_conv_prompt import task_conv

queries = {
    'task_add': task_add,
    'task_mult': task_mult,
    'task_inner': task_inner,
    'task_matmul': task_matmul,
    'task_conv': task_conv,
}