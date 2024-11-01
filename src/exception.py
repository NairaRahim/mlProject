'''
Manage all the exceptions of the project custom code
'''
import sys
import logging

def error_msg_detail(error, error_detail:sys):
    #error_detail is present inside sys
    _,_,exc_tb= error_detail.exc_info()# execution details first2 not needed
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_msg= 'Error occured in Python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, error
    )  

    return error_msg

'''
custom exception class inheriting from Exception class
'''
class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys) :
        super().__init__(error_msg)
        self.error_msg= error_msg_detail(error_msg, error_detail=error_detail)


    def __str__(self):
        return self.error_msg    


#for testing
# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('Divide by zero.')
#         raise CustomException(e, sys)