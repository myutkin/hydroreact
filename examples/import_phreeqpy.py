import phreeqpy.iphreeqc.phreeqc_dll as phreeqc_mod
import pandas as pd


#%% PHREEQC setup

phc1 = phreeqc_mod.IPhreeqc('/home/yutkinm/IPHREEQC/lib/libiphreeqc.so')
db_path = "/home/yutkinm/IPHREEQC/share/doc/iphreeqc/database/phreeqc.dat"
phc1.load_database(db_path)

def get_so(iph):
    out = iph.get_selected_output_array()
    return pd.DataFrame(out[1:], columns=out[0])

#%%

pc_input = """

SELECTED_OUTPUT 1
reset true

SOLUTION 1
END
"""

phc1.run_string(pc_input)

output = get_so(phc1)

print(output)