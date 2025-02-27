def caca(message):
    string = ""
    boolean = False
    carac_used = ""

    while boolean == False:
        string = input(f"{message} (pas de caracteres identiques) ")
        i = 0
        carac_used = ""
        boolean = True   
        while i <= len(string) - 1:
            if string[i] in carac_used:
                boolean = False

            elif boolean == True:
                carac_used += f"{string[i]}"
                boolean = True
            
            i += 1

    return string