#include <Python.h>

/**
 * print_python_bytes - prints information about Python bytes object
 * @p: PyObject (Python bytes object)
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes = (PyBytesObject *)p;
Py_ssize_t size, i;
char *string;
printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = PyBytes_Size(p);
string = PyBytes_AsString(p);
printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);
printf("  first 10 bytes: ");
for (i = 0; i < size && i < 10; i++)
{
printf("%02x", (unsigned char)string[i]);
if (i < size - 1 && i < 9)
printf(" ");
}
printf("\n");
}

/**
 * print_python_list - prints information about Python list object
 * @p: PyObject (Python list object)
 */
void print_python_list(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size, alloc, i;
printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}
size = PyList_Size(p);
alloc = list->allocated;
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", alloc);
for (i = 0; i < size; i++)
{
PyObject *element = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
if (PyBytes_Check(element))
print_python_bytes(element);
}
}

