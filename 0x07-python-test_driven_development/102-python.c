#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to a PyObject
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t size;
    Py_UNICODE *str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    size = PyUnicode_GetLength(p);
    str = PyUnicode_AsUnicode(p);

    printf("  type: %s\n", Py_TYPE(p)->tp_name);
    printf("  length: %ld\n", size);
    printf("  value: %ls\n", str);

    /* Do not forget to free the memory allocated by PyUnicode_AsUnicode() */
    PyMem_Free(str);
}
