def add_task(tasks, title):
    """
    Agrega una nueva tarea a la lista de tareas.

    Antes de crear la tarea, verifica que no exista otra con el mismo
    título (sin distinguir mayúsculas y minúsculas). Si el título ya
    existe, muestra un mensaje de error y no agrega la tarea.

    Args:
        tasks (list): Lista de tareas existentes.
        title (str): Título de la nueva tarea.

    Returns:
        None
    """
    # Verificar si ya existe una tarea con el mismo título
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Error: ya existe una tarea con ese título")
            return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("✅ Tarea agregada")


def list_tasks(tasks):
    """
    Muestra en consola todas las tareas registradas.

    Si la lista está vacía, informa al usuario que no hay tareas.
    En caso contrario, imprime cada tarea mostrando su ID, título
    y estado de completado.

    Args:
        tasks (list): Lista de tareas existentes.

    Returns:
        None
    """
    if not tasks:
        print("No hay tareas")
        return

    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'{task["id"]}. {task["title"]} [{status}]')


#  FUNCIÓN DE VALIDACIÓN DE ID
def validar_task_id(task_id):
    """
    Valida que el task_id:
    - Sea un número
    - No sea negativo
    - No rompa el programa si es inválido
    """
    try:
        task_id = int(task_id)
    except ValueError:
        print("❌ Error: El ID debe ser un número (no letras ni símbolos).")
        return None

    if task_id < 0:
        print("❌ Error: El ID no puede ser negativo.")
        return None

    return task_id


def complete_task(tasks, task_id):
    """
    Marca una tarea como completada.

    Valida el ID utilizando la función `validar_task_id`. Si el ID
    es inválido, la función termina sin interrumpir el flujo del
    programa. Si se encuentra la tarea correspondiente, cambia su
    estado a completado. Si no existe una tarea con ese ID, muestra
    un mensaje de error.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea a completar.

    Returns:
        None
    """
    task_id = validar_task_id(task_id)
    if task_id is None:
        return  # 🔁 No se rompe el menú

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("✅ Tarea marcada como completada")
            return

    print("❌ Error: No se encontró una tarea con ese ID")


def delete_task(tasks, task_id):
    """
    Elimina una tarea de la lista de tareas.

    Valida el ID utilizando la función `validar_task_id`. Si el ID
    es inválido, la función termina sin interrumpir el flujo del
    programa. Si la tarea existe, deberá ser eliminada del listado.
    Si no se encuentra una tarea con el ID proporcionado, se mostrará
    un mensaje de error.

    Args:
        tasks (list): Lista de tareas existentes.
        task_id (int | str): Identificador de la tarea a eliminar.

    Returns:
        None
    """
    task_id = validar_task_id(task_id)
    if task_id is None:
        return  # 🔁 No se rompe el menú
