#!/bin/bash
# Meshing procedure for the four-rotored tank simulation using the sliding mesh method
rm -r 0
rm -r master
rm -r inner
rm -r bottom
rm -r constant
rm -r system
rm -r slave
# For 4 processors
rm -r processor0
rm -r processor1
rm -r processor2
rm -r processor3

mkdir master
mkdir inner
mkdir bottom
mkdir constant
mkdir system

cp -r ./constant.orig/* ./constant/
cp -r ./system.orig/* ./system/

mkdir ./master/constant
mkdir ./master/system

cp -r ./constant.orig/* ./master/constant/
cp -r ./system.orig/* ./master/system/

cp -r ./master/* ./inner/
cp -r ./master/* ./bottom/

gmsh -format msh2 tank.geo -3 -o tank.msh
gmsh -format msh2 bottom.geo -3 -o bottom.msh
gmsh -format msh2 inner.geo -3 -o inner.msh

gmshToFoam tank.msh
cp -r ./constant/polyMesh ./master/constant/
rm -r ./constant/polyMesh

gmshToFoam bottom.msh
cp -r ./constant/polyMesh ./bottom/constant/
rm -r ./constant/polyMesh

gmshToFoam inner.msh
cp -r ./constant/polyMesh ./inner/constant/
rm -r ./constant/polyMesh

rm -r tank.msh
rm -r inner.msh
rm -r bottom.msh

mergeMeshes -overwrite master bottom
mergeMeshes -overwrite master inner 

cd ./master
stitchMesh -overwrite -perfect internalToMerge1 internalToMerge2
stitchMesh -overwrite -perfect internalToMerge3 internalToMerge4

sed -i 's/patch/wall/' ./constant/polyMesh/boundary
sed -i '17d' ./constant/polyMesh/boundary
sed -i '17i 4' ./constant/polyMesh/boundary
sed -i '19,46d;68,74d;82,95d' ./constant/polyMesh/boundary

cd ./../

rm -r constant/*
rm -r system/*
rm -r inner
rm -r bottom
cp -r ./master/constant/* ./constant
cp -r ./master/system/* ./system
rm -r master

mkdir ./0
cp ./0.orig/* ./0/

createBaffles -overwrite

topoSet

setFields

#decomposePar 
#mpirun -np 4 multiphaseEulerFoam -parallel > log &












  



