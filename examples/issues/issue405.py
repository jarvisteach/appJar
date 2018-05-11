import sys
sys.path.append("../../")

from appJar import gui

def validate(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if action == "1":
        if text in '0123456789.-+':
            try:  
                if len(str(value_if_allowed)) == 1 and value_if_allowed in '.-': 
                    return True
                elif len(str(value_if_allowed)) == 2 and value_if_allowed == '-.': 
                    return True
                else: 
                    float(value_if_allowed)
                    return True
            except ValueError:
                app.bell()
                return False 
        else: 
            app.bell()
            return False 
    else: 
        return True

with gui() as app:
    ent = app.entry('e1')

    validator = (app.topLevel.register(validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    ent.config(validate='key', validatecommand=validator)
