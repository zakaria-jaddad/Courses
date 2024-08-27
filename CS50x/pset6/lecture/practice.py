from cs50 import get_string

c = get_string("do you agree wiht me ?").lower()


if c in ["y", "yes"]:


    print("yes you do")


elif c in ["n", "no"]:


    print("you don't")
