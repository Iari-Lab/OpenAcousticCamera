e = 0.65;
radius = 0.3/2;
color ("gray") {
    for(j=[0:20]) 
        {
        for (i = [0:20]){
            translate([i*e,j*e,radius]) {
                sphere(r = radius, $fn=20, center=true);
                }
       }
    }
}

color ("black") {
    translate([-0.5,-0.5,0.21]) {        
        cube( [14,14,0.96] );
    }
}
