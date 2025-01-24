def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    f.write('some data') #this line might not be executed if an exception occurs before this line
    #this line is also important in the sense that we should close the file whether there is an exception or not

#this function is also important because it shows the use of the try-except-finally block which is a good practice in programming
#in exception handling
#the finally block is always executed regardless of whether there is an exception or not
#this is important for the closing of the file
def function_with_unclosed_file_solution(filename):
    try:
        f = open(filename, 'w')
        # ... some code that might raise an exception ...
        f.write('some data')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        f.close()
        print('File closed')