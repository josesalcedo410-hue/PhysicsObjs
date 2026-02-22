
#ifndef SIMPLE_FUNCTIONS_H
#define SIMPLE_FUNCTIONS_H

#include "Dipole.h"

Vector addVectors(Vector a, Vector b){
    Vector result;
    result.x = a.x + b.x;
    result.y = a.y + b.y;
    result.z = a.z + b.z;
    return result;
}

Vector subVectors(Vector a, Vector b){
    Vector result;
    result.x = a.x - b.x;
    result.y = a.y - b.y;
    result.z = a.z - b.z;
    return result;
}

Vector scaleVector(Vector v, float scalar){
    Vector result;
    result.x = v.x * scalar;
    result.y = v.y * scalar;
    result.z = v.z * scalar;
    return result;
}

double magnitude(Vector v){
    return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}

Vector dipole(Dipole d){
    return scaleVector(d.dir, d.charge);
}

#endif // SIMPLE_FUNCTIONS_H