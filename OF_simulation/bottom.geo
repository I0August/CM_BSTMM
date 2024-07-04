Geometry.CopyMeshingMethod = 1;
dTank =2.09;
rTank =1.045;
hTank =7.550059999999999;
hemiRatio =2.213514;
dImpeller =0.6966666666666665;
rImpeller =0.3483333333333333;
rRod =0.05573333333333332;
hRod =0.08791548165812377;
rDish =0.25079999999999997;
lBlade =0.17416666666666664;
wBlade =0.1393333333333333;
hImpeller =0.6479309816581238;
delhImpeller =1.449833;
wBaffle =0.16699099999999997;
rRotatingZone =0.40058333333333324;
hRotatingZone =0.2786666666666666;
xHemiBottom1 =-0.5179304029944437;
zHemiBottom1 =-0.2523473249317676;
xHemiBottom2 =-0.288453507212936;
zHemiBottom2 =-0.2926343645790717;
xHemiBottom3 =-0.6380863095109114;
zHemiBottom3 =-0.38163264429209875;
xHemiBottom4 =-0.3506802508355969;
zHemiBottom4 =-0.45062888940997764;
nx1 =20;
nx2 =20;
nx3 =20;
nx4 =20;
nyAboveDish =10;
nyBelowDish =10;
nxyAroundBlade =10;
nyTop =30;
nyBottom =15;
nyHemiBottom =10;
nyRod =5;
nyGap =30;
nr =5;

Point(1) ={-rRod,0,0};
Point(2) ={-rRod, 0, -rTank/hemiRatio + wBaffle};
Point(3) ={-rRod, 0, -rTank/hemiRatio};
Point(4) ={-rDish, 0, 0};
Point(5) ={-rRotatingZone, 0, 0};
Point(6) ={-rTank+wBaffle,0,0};
Point(7) ={-rTank,0,0};
Point(8) ={xHemiBottom1, 0, zHemiBottom1};
Point(9) ={xHemiBottom2, 0, zHemiBottom2};
Point(10) ={xHemiBottom3, 0, zHemiBottom3};
Point(11) ={xHemiBottom4, 0, zHemiBottom4};
Point(12) ={-rRod, 0, (-rTank/hemiRatio + wBaffle)/2};
Point(13) ={-rDish, 0, (-rTank/hemiRatio + wBaffle)/2};
Point(14) ={-rRotatingZone, 0, (-rTank/hemiRatio + wBaffle)/2};
Ellipse(1) ={6,1,6,8};
Ellipse(2) ={8,1,6,9};
Ellipse(3) ={9,1,6,2};
Ellipse(4) ={7,1,7,10};
Ellipse(5) ={10,1,7,11};
Ellipse(6) ={11,1,7,3};
Line(7) ={1, 12};
Line(8) ={12, 2};
Line(9) ={2, 3};
Line(10) ={4, 13};
Line(11) ={13, 9};
Line(12) ={9, 11};
Line(13) ={5,14};
Line(14) ={14, 8};
Line(15) ={8, 10};
Line(16) ={1, 4};
Line(17) ={4, 5};
Line(18) ={5, 6};
Line(19) ={6, 7};
Line(20) ={12, 13};
Line(21) ={13, 14};
Curve Loop(1) ={9,-6,-12,3};
Plane Surface(1) ={1};
Curve Loop(2) ={8,-3,-11,-20};
Plane Surface(2) ={2};
Curve Loop(3) ={7,20,-10,-16};
Plane Surface(3) ={3};
Curve Loop(4) ={12,-5,-15,2};
Plane Surface(4) ={4};
Curve Loop(5) ={11,-2,-14,-21};
Plane Surface(5) ={5};
Curve Loop(6) ={10,21,-13,-17};
Plane Surface(6) ={6};
Curve Loop(7) ={15,-4,-19,1};
Plane Surface(7) ={7};
Curve Loop(8) ={13,14,-1,-18};
Plane Surface(8) ={8};
Transfinite Curve {19,15,12,9} = nx1 Using Progression 1;
Transfinite Curve {18,14,11,8} = nx2 Using Progression 1;
Transfinite Curve {17,21,2,5} = nx3 Using Progression 1;
Transfinite Curve {16,20,3,6} = nx4 Using Progression 1;
Transfinite Curve {1,4,7,10,13} = nyHemiBottom Using Progression 1;Transfinite Surface {1};
Transfinite Surface {2};
Transfinite Surface {3};
Transfinite Surface {4};
Transfinite Surface {5};
Transfinite Surface {6};
Transfinite Surface {7};
Transfinite Surface {8};
Recombine Surface {1,2,3,4,5,6,7,8};


//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{3}; Surface{2}; Surface{1}; Surface{6}; Surface{5}; Surface{4}; Surface{8}; Surface{7}; 
Layers{nr}; Recombine;}

//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{43}; Surface{65}; Surface{87}; Surface{109}; Surface{131}; Surface{153}; Surface{175}; Surface{197}; Layers{nr}; Recombine;}

//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{219}; Surface{241}; Surface{263}; Surface{285}; Surface{307}; Surface{329}; Surface{351}; Surface{373}; Layers{nr}; Recombine;
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{395}; Surface{417}; Surface{439}; Surface{505}; Surface{483}; Surface{461}; Surface{527}; Surface{549}; Layers{nr}; Recombine;
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{615}; Surface{593}; Surface{571}; Surface{637}; Surface{659}; Surface{681}; Surface{703}; Surface{725}; Layers{nr}; Recombine;
}

//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{791}; Surface{769}; Surface{747}; Surface{813}; Surface{835}; Surface{857}; Surface{879}; Surface{901}; Layers{nr}; Recombine; 
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{923}; Surface{945}; Surface{967}; Surface{989}; Surface{1011}; Surface{1033}; Surface{1055}; Surface{1077}; Layers{nr}; Recombine;
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{1121}; Surface{1099}; Surface{1143}; Surface{1165}; Surface{1187}; Surface{1209}; Surface{1231}; Surface{1253}; Layers{nr}; Recombine;
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{1297}; Surface{1275}; Surface{1319}; Surface{1385}; Surface{1363}; Surface{1341}; Surface{1429}; Surface{1407}; Layers{nr}; Recombine; 
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{1451}; Surface{1473}; Surface{1495}; Surface{1517}; Surface{1539}; Surface{1561}; Surface{1605}; Surface{1583}; Layers{nr}; Recombine; 
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{1627}; Surface{1649}; Surface{1671}; Surface{1693}; Surface{1715}; Surface{1737}; Surface{1759}; Surface{1781}; Layers{nr}; Recombine;
}
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{1803}; Surface{1825}; Surface{1847}; Surface{1869}; Surface{1891}; Surface{1913}; Surface{1935}; Surface{1957}; Layers{nr}; Recombine;
}

//+
Physical Surface("internalToMerge1", 2106) = {544, 526, 460, 394, 570, 790, 922, 1098, 1296, 1450, 1626, 1802, 1978, 42, 218, 680, 856, 1032, 1208, 1384, 1516, 1692, 1868, 2033, 108, 284, 702, 878, 1054, 1230, 1406, 1604, 1758, 1934, 2088, 174, 350, 720, 896, 1072, 1248, 1424, 1578, 1776, 1952, 2105, 192, 368};
//+
Physical Surface("wall", 2107) = {892, 804, 738, 716, 628, 606, 430, 496, 540, 364, 320, 254, 78, 144, 188, 2101, 2063, 2008, 1838, 1904, 1948, 1772, 1728, 1662, 1486, 1552, 1574, 1420, 1332, 1310, 1134, 1156, 1244, 1068, 980, 958};
//+
Physical Surface("internalToMerge3", 2108) = {1636, 1834, 1658, 1614, 1790, 1812, 1987, 1966, 2004, 30, 52, 74, 206, 228, 250, 382, 404, 426, 558, 580, 602, 778, 756, 734, 910, 932, 954, 1086, 1108, 1130, 1284, 1262, 1306, 1482, 1460, 1438};

Physical Volume("tank") = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96};
