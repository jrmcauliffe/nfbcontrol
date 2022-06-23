include <./includes.scad>

keyNames = ["1", "2", "A", "B","!","A","B","C","▲","▼","►","◄"];
// example key
for(n = [0:len(keyNames)-1]) {
    translate_u(, n) dsa_row(3) legend(keyNames[n], size=8) key();
}

