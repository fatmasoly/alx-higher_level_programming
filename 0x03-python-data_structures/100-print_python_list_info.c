#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: PyObject pointer representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size, allocated, i;
PyTypeObject *type;
size = Py_SIZE(p);
allocated = list->allocated;
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);
for (i = 0; i < size; ++i)
{
type = Py_TYPE(list->ob_item[i]);
printf("Element %ld: %s\n", i, type->tp_name);
}
}

