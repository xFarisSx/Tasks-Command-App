from argparse import *
from .TaskController import TaskController

def main():
    controller = TaskController('tasks.txt')


    parser  = ArgumentParser(description='Simple CLI Task Manager')
    subparsers = parser.add_subparsers()
    add_task = subparsers.add_parser("add",help = 'add the given task')

    add_task.add_argument('title',help='title of the task',type=str)
    add_task.add_argument('-d','--description',help='short description of the task',type=str,default=None)
    add_task.add_argument('-s','--start_date',help='date to begin the task',type=str,default=None)
    add_task.add_argument('-e','--end_date',help='date to end the task',type=str,default=None)
    add_task.add_argument('--done',help='check wether the task is done or not',default=False)

    add_task.set_defaults(func = controller.add_task)

    list_tasks = subparsers.add_parser('list',help='list unfinished tasks')
    list_tasks.add_argument('-a','--all',help='list all the tasks', action='store_true')
    list_tasks.set_defaults(func= controller.display)


    check_task = subparsers.add_parser('check',help='check the given task')
    check_task.add_argument('-t','--task',help='number of the task to be done,if not specified,last task will be removed',type=int)
    check_task.set_defaults(func = controller.check_tasks)

    remove = subparsers.add_parser('remove',help='Remove a task')
    remove.add_argument('-t','--task',help='the task to be removed (number)',type=int)
    remove.set_defaults(func = controller.remove)

    reset = subparsers.add_parser('reset',help='remove all tasks')
    reset.set_defaults(func = controller.restart)

    args = parser.parse_args()
    args.func(args)



if __name__ == '__main__':
    main()