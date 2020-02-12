#Processes all other errors

v0_errors = {1 : "Error with head section. Please add either \"Line #\" "+\
               "or \"DivLine\" to the indicated line.\nPlease make sure"+\
               " to format these exactly as shown.\n" +\
               "If this line belongs in the body, please remember to put"+\
               " a space before it.\n",
             2 : "This line belongs in the head. If you meant for this to "+\
               "be in the head," +\
               " there may be an issue with the spacing.\nMake sure there "+\
               "are no spaces between the lines \"Page #:\" and \"Margin:\""+\
               " and that you don't use double spacing.\n"+\
               "If this is a diary entry header, make sure to use \"*\" " +\
               "rather than \"DivLine\".\nIf this is a journey header, add "+\
               " the line \"Text:\" before it.\n",
             3 : "This line should be a journey header. If it is, please make "+\
               "sure to begin it with \"Line #\". If not, please put in a "+\
               "journey header before this line.",
             4 : "Lines cannot be formatted like \"Line #, #, #:\" or "+\
               "\"Lines #-#\" or any similar format.\nEach part of the"+\
               "line must get its own line and must begin with \"Line #:\".\n",
             5 : "This line must be formatted \"Page #\". No additional "+\
               "formatting is allowed.\n"}
               
v1_errors = {1 : "Error with head section. Please add \"Margin Line #\" "+\
               "to the indicated line.\nPlease make sure"+\
               " to format these exactly as shown.\n" +\
               "If this line belongs in the body, please remember to put"+\
               " a space before it.\n",
             2 : "This line belongs in the head. If you meant for this to "+\
               "be in the head," +\
               " there may be an issue with the spacing.\nMake sure there "+\
               "are no spaces between the lines \"Page #:\" and \"Notes:\""+\
               " and that you don't use double spacing.\n"+\
               "If this is a diary entry header, make sure to use \"*\" " +\
               "rather than \"DivLine\".\nIf this is a journey header, add "+\
               " the line \"Text:\" before it.\n",
             3 : "This line should be a journey header. If it is, please make "+\
               "sure to begin it with \"Section:\". If not, please put in a "+\
               "journey header before this line.",
             4 : "Lines cannot be formatted like \"Line #, #, #:\" or "+\
               "\"Lines #-#\" or any similar format.\nEach part of the"+\
               "line must get its own line and must begin with \"Line #:\".\n",
             5 : "This line must be formatted \"Page #\". No additional "+\
               "formatting is allowed.\n"}
               
def errors(page_num, line_num, line, error_code, version):
  """Produces an error message. Contains the line and page number, the
  faulty line, and what the error is."""

  err_str = "An error was found on page " + str(page_num) +\
            ", line " +  str(line_num + 1) + ": " + line.strip()

  if version == 0:
    err_str += v0_errors[error_code]
  elif version == 1:
    err_str += v1_err[error_code]
  #else
  
  
  #######
  if error_code == 1:
    err_str += "Error with head section. Please add either \"Line #\" "+\
               "or \"DivLine\" to the indicated line.\nPlease make sure"+\
               " to format these exactly as shown.\n" +\
               "If this line belongs in the body, please remember to put"+\
               " a space before it.\n"
  elif error_code == 2:
    err_str += "This line belongs in the head. If you meant for this to "+\
               "be in the head," +\
               " there may be an issue with the spacing.\nMake sure there "+\
               "are no spaces between the lines \"Page #:\" and \"Margin:\""+\
               " and that you don't use double spacing.\n"+\
               "If this is a diary entry header, make sure to use \"*\" " +\
               "rather than \"DivLine\".\nIf this is a journey header, add "+\
               " the line \"Text:\" before it.\n"
  elif error_code == 3:
    err_str += "This line should be a journey header. If it is, please make "+\
               "sure to begin it with \"Line #\". If not, please put in a "+\
               "journey header before this line."
  elif error_code == 4:
    err_str += "Lines cannot be formatted like \"Line #, #, #:\" or "+\
               "\"Lines #-#\" or any similar format.\nEach part of the"+\
               "line must get its own line and must begin with \"Line #:\".\n"
  elif error_code == 5:
    err_str += "This line must be formatted \"Page #\". No additional "+\
               "formatting is allowed.\n"
               
    #####
  return err_str