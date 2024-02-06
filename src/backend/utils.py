import pytest
import importlib
from typing import Dict, List, Tuple


def import_function_by_path(
    root_directory="data",
    user_name="user1",
    lab_name="task3.py",
    func_name="Task3"
    ):
    # Split the path into module name and function name
    module_name = '.'.join([root_directory, user_name, lab_name])

    # Import the module
    module = importlib.import_module(module_name)

    # Get the function from the module
    func = getattr(module, func_name)

    return func


def check_results(result: Tuple, target: Tuple) -> bool:
    matched = True
    error_list = []
    for i in range(len(result)):
        result_el = result[i]
        target_el = target[i]
        if isinstance(target_el, str) or isinstance(target_el, bool):
            if result_el != target_el:
                matched = False
                error_list.append((result_el, target_el))
        else:
            if isinstance(target_el, tuple): 
                if result_el < target_el[0] or result_el > target_el[1]:
                    matched = False
                    error_list.append((result_el, target_el))
            else:
                if result_el != target_el:
                    matched = False
                    error_list.append((result_el, target_el))

    return matched, error_list


def test_func(func, input_params_list: List[Dict], target_results: Tuple):
    task_success = True
    task_error_list = []
    for param_ind, input_params in enumerate(input_params_list):
        func_result = func(input_params)
        params_check_result, params_check_error_list = check_results(func_result, target_results[param_ind])
        if not params_check_result:
            task_success = False
            task_error_list.append(params_check_error_list)

    return task_success, task_error_list

    
def check_lab(
    root_directory,
    user_name,
    lab_name,
    func_name,
    input_params,
    target_results
    ):
    func = import_function_by_path(root_directory, user_name, lab_name, func_name)
    result_code, task_error_list = test_func(func, input_params, target_results)
    print(func_name, result_code, task_error_list)
    return result_code


if __name__=="__main__":
    check_lab("src.test.data", "user1", "task3", "Task3",
                [{"a": 144}, {"a": 0}], (((12-1e-3,12+1e-3),), (((-1e-3,1e-3),))))
    check_lab("src.test.data", "user1", "task3", "Task4",
                [{"a": [0, 1]}, {"a": [1, 0]}],
                ((123, True, 'abc'), (123, False, 'abc'))
                )