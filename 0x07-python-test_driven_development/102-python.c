#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @str_obj: A PyObject string object.
 */
void print_python_string(PyObject *str_obj)
{
    long int length;

    fflush(stdout);

    printf("[INFO] String object details:\n");

    if (strcmp(str_obj->ob_type->tp_name, "str") != 0)
    {
        printf("[ERROR] Not a valid string object.\n");
        return;
    }

    length = ((PyASCIIObject *)(str_obj))->length;

    if (PyUnicode_IS_COMPACT_ASCII(str_obj))
        printf("[INFO] Type: compact ascii\n");
    else
        printf("[INFO] Type: compact unicode object\n");

    printf("[INFO] Length: %ld\n", length);
    printf("[INFO] Value: %ls\n", PyUnicode_AsWideCharString(str_obj, &length));
}
