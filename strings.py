# ordered , immutable, text reresentation

# when you want to use ' you need to use "" or \'

# """ """ this is for multi line string

# --------------------
# my_string = "Hello"
# char = my_string[0] # index the first letter
# print(char)

# a = "abcd"
# # b =a[0:2] #(0~1)
# #c = a[::2] #(0,2)
# # print(c)

#------------------
# greeting = "Hello"
# name = "Tom"
# sent = greeting + " " + name
# print(sent)

# mystr = "          he   l  "
# mystr.strip()
# mystr = mystr.strip() # strip works only here
# print(mystr)

# # --------------------
# mystring = "hello"
# print(mystring.startswith("h")) #True
# print(mystring.endswith("h"))   #False
# print(mystring.find("h")) #show the index
# print(mystring.count("h")) #count the num
# print(mystring.replace("he","se")) #replace


#---------------------
# from timeit import default_timer as timer
# my_list = ["a"] * 100


# #bad
# start = timer()
# mystr = ''
# for i in my_list:
#     mystr += i
# stop = timer()
# print(stop - start)

# #ggod
# start= timer()
# mystr = ''.join(my_list)
# stop = timer()
# print(stop - start)


# --------------
# var = "Tom"
# mystr = "the var is %s" % var #instead %s to % var
# print(mystr)

#-----------
# var = 3
# myst = "the var is %d " % var
# print(myst)

#------------
# var = 3.141592
# ms = "the var is %f " % var
# ss = "the var is %.2f" % var
# print(ms)
# print(ss)

#----------
# var = 3.123123
# var2 = "Bam"
# ms = "the var is {:.1f} and {}".format(var, var2) # same with %
# ms = f"the var is {var} , {var2}"
