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
Point(2) ={-rDish, 0, 0};
Point(3) ={-rRotatingZone, 0, 0};
Point(4) ={-rTank+wBaffle,0,0};
Point(5) ={-rTank,0,0};

Point(6) = {-rRod, 0, hRod};
Point(7) = {-rDish, 0, hRod};
Point(8) = {-rRotatingZone, 0, hRod};
Point(9) = {-rTank + wBaffle, 0, hRod};
Point(10) = {-rTank, 0, hRod};

Point(11) = {-rTank + wBaffle, 0, hImpeller};
Point(12) = {-rTank, 0, hImpeller};
Point(13) = {-rTank + wBaffle, 0, hImpeller - hRotatingZone/2};
Point(14) = {-rTank, 0, hImpeller - hRotatingZone/2};
Point(15) = {-rTank + wBaffle, 0, hImpeller + hRotatingZone/2};
Point(16) = {-rTank, 0, hImpeller + hRotatingZone/2};

Point(17) = {-rRod, 0, hImpeller};
Point(18) = {-rRod, 0, hImpeller - hRotatingZone/2};
Point(19) = {-rRod, 0, hImpeller + hRotatingZone/2};
Point(20) = {-rImpeller + lBlade, 0, hImpeller - wBlade/2};
Point(21) = {-rImpeller + lBlade, 0, hImpeller};
Point(22) = {-rImpeller + lBlade, 0, hImpeller + wBlade/2};
Point(23) = {-rDish, 0, hImpeller - wBlade/2};
Point(24) = {-rDish, 0, hImpeller};
Point(25) = {-rDish, 0, hImpeller + wBlade/2};
Point(26) = {-rImpeller, 0, hImpeller - wBlade/2};
Point(27) = {-rImpeller, 0, hImpeller};
Point(28) = {-rImpeller, 0, hImpeller + wBlade/2};
Point(29) = {-rRotatingZone, 0, hImpeller};
Point(30) = {-rRotatingZone, 0, hImpeller - hRotatingZone/2};
Point(31) = {-rRotatingZone, 0, hImpeller + hRotatingZone/2};
Point(32) = {-rRotatingZone, 0, 0};
Point(33) = {-rDish, 0, hImpeller + hRotatingZone/2};
Point(34) = {-rDish, 0, hImpeller - hRotatingZone/2};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 5};
//+
Line(5) = {6, 7};
//+
Line(7) = {7, 8};
//+
Line(8) = {8, 9};
//+
Line(9) = {9, 10};
//+
Line(10) = {1, 6};
//+
Line(11) = {2, 7};
//+
Line(12) = {3, 8};
//+
Line(13) = {4, 9};
//+
Line(14) = {5, 10};
//+
Line(15) = {18, 34};
//+
Line(16) = {34, 30};
//+
Line(17) = {30, 13};
//+
Line(18) = {13, 14};
//+
Line(19) = {17, 21};
//+
Line(20) = {21, 24};
//+
Line(21) = {24, 27};
//+
Line(22) = {27, 29};
//+
Line(23) = {29, 11};
//+
Line(24) = {11, 12};
//+
Line(25) = {19, 33};
//+
Line(26) = {33, 31};
//+
Line(27) = {31, 15};
//+
Line(28) = {15, 16};
//+
Line(29) = {18, 17};
//+
Line(30) = {17, 19};
//+
Line(31) = {20, 21};
//+
Line(32) = {21, 22};
//+
Line(33) = {22, 25};
//+
Line(34) = {25, 28};
//+
Line(35) = {28, 27};
//+
Line(36) = {27, 26};
//+
Line(37) = {26, 23};
//+
Line(38) = {23, 20};
//+
Line(39) = {34, 23};
//+
Line(40) = {23, 24};
//+
Line(41) = {24, 25};
//+
Line(42) = {25, 33};
//+
Line(43) = {30, 29};
//+
Line(44) = {29, 31};
//+
Line(45) = {13, 11};
//+
Line(46) = {11, 15};
//+
Line(47) = {14, 12};
//+
Line(48) = {12, 16};
//+
Line(49) = {18, 20};
//+
Line(50) = {19, 22};
//+
Line(51) = {31, 28};
//+
Line(52) = {30, 26};
//+
Line(53) = {6, 18};
//+
Line(54) = {7, 34};
//+
Line(55) = {8, 30};
//+
Line(56) = {9, 13};
//+
Line(57) = {10, 14};
//+
Curve Loop(1) = {10, 5, -11, -1};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {11, 7, -12, -2};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {12, 8, -13, -3};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {13, 9, -14, -4};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {53, 15, -54, -5};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {54, 16, -55, -7};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {55, 17, -56, -8};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {56, 18, -57, -9};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {29, 19, -31, -49};
//+
Plane Surface(9) = {9};

//+
Curve Loop(10) = {30, 50, -32, -19};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {49, -38, -39, -15};
//+
Plane Surface(11) = {11};
//+
Curve Loop(12) = {31, 20, -40, 38};
//+
Plane Surface(12) = {12};
//+
Curve Loop(13) = {32, 33, -41, -20};
//+
Plane Surface(13) = {13};
//+
Curve Loop(14) = {50, 33, 42, -25};
//+
Plane Surface(14) = {14};
//+
Curve Loop(15) = {39, -37, -52, -16};
//+
Plane Surface(15) = {15};
//+
Curve Loop(16) = {40, 21, 36, 37};
//+
Plane Surface(16) = {16};
//+
Curve Loop(17) = {41, 34, 35, -21};
//+
Plane Surface(17) = {17};
//+
Curve Loop(18) = {42, 26, 51, -34};
//+
Plane Surface(18) = {18};
//+
Curve Loop(19) = {52, -36, 22, -43};
//+
Plane Surface(19) = {19};
//+
Curve Loop(20) = {35, 22, 44, 51};
//+
Plane Surface(20) = {20};
//+
Curve Loop(21) = {43, 23, -45, -17};
//+
Plane Surface(21) = {21};
//+

//+
Curve Loop(22) = {44, 27, -46, -23};
//+
Plane Surface(22) = {22};
//+
Curve Loop(23) = {45, 24, -47, -18};
//+
Plane Surface(23) = {23};
//+
Curve Loop(24) = {46, 28, -48, -24};
//+
Plane Surface(24) = {24};
//+
Transfinite Curve {28, 24, 18, 9, 4} = nx1 Using Progression 1;
//+
Transfinite Curve {27, 23, 17, 8, 3} = nx2 Using Progression 1;
//+
Transfinite Curve {26, 34, 21, 37, 16, 7, 2} = nx3 Using Progression 1;
//+
Transfinite Curve {25, 33, 20, 38, 15, 5, 1} = nx4 Using Progression 1;
//+
Transfinite Curve {30, 32, 41, 35, 44, 46, 48} = nyAboveDish Using Progression 1;
//+
Transfinite Curve {29, 31, 40, 36, 43, 45, 47} = nyBelowDish Using Progression 1;
//+
Transfinite Curve {53, 54, 55, 56, 57} = nyBottom Using Progression 1;
//+
Transfinite Curve {10, 11, 12, 13, 14} = nyRod Using Progression 1;
//+
Transfinite Curve {50, 42, 51, 22, 52, 39, 49, 19} = nxyAroundBlade Using Progression 1;
//+

Transfinite Surface {1};
//+
Transfinite Surface {2};
//+
Transfinite Surface {3};
//+
Transfinite Surface {4};
//+
Transfinite Surface {5};
//+
Transfinite Surface {6};
//+
Transfinite Surface {7};
//+
Transfinite Surface {8};
//+
Transfinite Surface {9};
//+
Transfinite Surface {10};
//+
Transfinite Surface {11};
//+
Transfinite Surface {12};
//+
Transfinite Surface {13};
//+
Transfinite Surface {14};
//+
Transfinite Surface {15};
//+
Transfinite Surface {16};
//+
Transfinite Surface {17};
//+
Transfinite Surface {18};
//+
Transfinite Surface {19};
//+
Transfinite Surface {20};
//+
Transfinite Surface {21};
//+
Transfinite Surface {22};
//+
Transfinite Surface {23};
//+
Transfinite Surface {24};
//+
Recombine Surface {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24};
//+
Translate {0, 0, delhImpeller} {
  Duplicata { Surface{9}; Surface{10}; Surface{14}; Surface{11}; Surface{12}; Surface{13}; Surface{15}; Surface{16}; Surface{17}; Surface{18}; Surface{19}; Surface{20}; Surface{21}; Surface{22}; Surface{23}; Surface{24}; }
}

Translate {0, 0, delhImpeller*2} {
  Duplicata { Surface{9}; Surface{10}; Surface{14}; Surface{11}; Surface{12}; Surface{13}; Surface{15}; Surface{16}; Surface{17}; Surface{18}; Surface{19}; Surface{20}; Surface{21}; Surface{22}; Surface{23}; Surface{24}; }
}

Translate {0, 0, delhImpeller*3} {
  Duplicata { Surface{9}; Surface{10}; Surface{14}; Surface{11}; Surface{12}; Surface{13}; Surface{15}; Surface{16}; Surface{17}; Surface{18}; Surface{19}; Surface{20}; Surface{21}; Surface{22}; Surface{23}; Surface{24}; }
}

Point(newp) = {-rRod, 0, hTank};
Point(newp) = {-rDish, 0, hTank};
Point(newp) = {-rRotatingZone, 0, hTank};
Point(newp) = {-rTank + wBaffle, 0, hTank};
Point(newp) = {-rTank, 0, hTank};

//+
Line(295) = {773, 774};
//+
Line(296) = {774, 775};
//+
Line(297) = {775, 776};
//+
Line(298) = {776, 777};
//+
Line(299) = {19, 35};
//+
Line(300) = {33, 92};
//+
Line(301) = {31, 140};
//+
Line(302) = {15, 236};
//+
Line(303) = {16, 268};
//+
Line(304) = {52, 281};
//+
Line(305) = {76, 338};
//+
Line(306) = {184, 386};
//+
Line(307) = {248, 482};
//+
Line(308) = {280, 514};
//+
Line(309) = {298, 527};
//+
Line(310) = {322, 584};
//+
Line(311) = {430, 632};
//+
Line(312) = {494, 728};
//+
Line(313) = {526, 760};
//+
Line(314) = {544, 773};
//+
Line(315) = {568, 774};
//+
Line(316) = {676, 775};
//+
Line(317) = {740, 776};
//+
Line(318) = {772, 777};
//+
Curve Loop(25) = {299, -77, -300, -25};
//+
Plane Surface(292) = {25};
//+
Curve Loop(26) = {300, -92, -301, -26};
//+
Plane Surface(293) = {26};
//+
Curve Loop(27) = {301, -122, -302, -27};
//+
Plane Surface(294) = {27};
//+
Curve Loop(28) = {302, -132, -303, -28};
//+
Plane Surface(295) = {28};
//+
Curve Loop(29) = {304, -156, -305, 72};
//+
Plane Surface(296) = {29};
//+
Curve Loop(30) = {305, -171, -306, -105};
//+
Plane Surface(297) = {30};
//+
Curve Loop(31) = {306, -201, -307, -125};
//+
Plane Surface(298) = {31};
//+
Curve Loop(32) = {307, -211, -308, -135};
//+
Plane Surface(299) = {32};
//+
Curve Loop(33) = {309, -235, -310, 151};
//+
Plane Surface(300) = {33};
//+
Curve Loop(34) = {310, -250, -311, -184};
//+
Plane Surface(301) = {34};
//+
Curve Loop(35) = {311, -280, -312, -204};
//+
Plane Surface(302) = {35};
//+
Curve Loop(36) = {312, -290, -313, -214};
//+
Plane Surface(303) = {36};
//+
Curve Loop(37) = {314, 295, -315, 230};
//+
Plane Surface(304) = {37};
//+
Curve Loop(38) = {315, 296, -316, -263};
//+
Plane Surface(305) = {38};
//+
Curve Loop(39) = {316, 297, -317, -283};
//+
Plane Surface(306) = {39};
//+
Curve Loop(40) = {317, 298, -318, -293};
//+
Plane Surface(307) = {40};
//+
Transfinite Curve {299, 300, 301, 302, 303} = nyGap Using Progression 1;
//+
Transfinite Curve {304, 305, 306, 307, 308} = nyGap Using Progression 1;
//+
Transfinite Curve {309, 310, 311, 312, 313} = nyGap Using Progression 1;
//+
Transfinite Curve {314, 315, 316, 317, 318} = nyTop Using Progression 1;

Transfinite Curve {298} = nx1 Using Progression 1;
//+
Transfinite Curve {297} = nx2 Using Progression 1;
//+
Transfinite Curve {296} = nx3 Using Progression 1;
//+
Transfinite Curve {295} = nx4 Using Progression 1;
//+
Transfinite Surface {292};
//+
Transfinite Surface {293};
//+
Transfinite Surface {294};
//+
Transfinite Surface {295};
//+
Transfinite Surface {296};
//+
Transfinite Surface {297};
//+
Transfinite Surface {298};
//+
Transfinite Surface {299};
//+
Transfinite Surface {300};
//+
Transfinite Surface {301};
//+
Transfinite Surface {302};
//+
Transfinite Surface {303};
//+
Transfinite Surface {304};
//+
Transfinite Surface {305};
//+
Transfinite Surface {306};
//+
Transfinite Surface {307};
//+

//+
Recombine Surface {292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307};
//+
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Surface{6}; Surface{7}; Surface{8}; Surface{9}; Surface{10}; Surface{11}; Surface{12}; Surface{13}; Surface{14}; Surface{15}; Surface{16}; Surface{17}; Surface{18}; Surface{19}; Surface{20}; Surface{21}; Surface{22}; Surface{23}; Surface{24}; Surface{292}; Surface{293}; Surface{294}; Surface{295}; Surface{73}; Surface{58}; Surface{63}; Surface{68}; Surface{83}; Surface{78}; Surface{93}; Surface{98}; Surface{103}; Surface{88}; Surface{108}; Surface{113}; Surface{123}; Surface{118}; Surface{128}; Surface{133}; Surface{299}; Surface{298}; Surface{297}; Surface{296}; Surface{137}; Surface{142}; Surface{147}; Surface{162}; Surface{157}; Surface{152}; Surface{167}; Surface{172}; Surface{177}; Surface{182}; Surface{192}; Surface{187}; Surface{197}; Surface{202}; Surface{207}; Surface{212}; Surface{300}; Surface{301}; Surface{302}; Surface{303}; Surface{216}; Surface{221}; Surface{226}; Surface{236}; Surface{241}; Surface{231}; Surface{246}; Surface{251}; Surface{256}; Surface{261}; Surface{266}; Surface{271}; Surface{276}; Surface{281}; Surface{286}; Surface{291}; Surface{304}; Surface{305}; Surface{306}; Surface{307}; Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
  Surface{340};Surface{362}; Surface{384}; Surface{406}; Surface{428}; Surface{450}; Surface{472}; Surface{494}; Surface{516}; Surface{538}; Surface{560}; Surface{582}; Surface{604}; Surface{626}; Surface{648}; Surface{670}; Surface{692}; Surface{714}; Surface{736}; Surface{758}; Surface{780}; Surface{802}; Surface{824}; Surface{846}; Surface{868}; Surface{890}; Surface{912}; Surface{934}; Surface{956}; Surface{978}; Surface{1000}; Surface{1022}; Surface{1044}; Surface{1066}; Surface{1088}; Surface{1110}; Surface{1132}; Surface{1154}; Surface{1176}; Surface{1198}; Surface{1220}; Surface{1242}; Surface{1264}; Surface{1286}; Surface{1308}; Surface{1330}; Surface{1352}; Surface{1374}; Surface{1396}; Surface{1418}; Surface{1440}; Surface{1462}; Surface{1484}; Surface{1506}; Surface{1528}; Surface{1550}; Surface{1572}; Surface{1594}; Surface{1616}; Surface{1638}; Surface{1660}; Surface{1682}; Surface{1704}; Surface{1726}; Surface{1748}; Surface{1770}; Surface{1792}; Surface{1814}; Surface{1836}; Surface{1858}; Surface{1880}; Surface{1902}; Surface{1924}; Surface{1946}; Surface{1968}; Surface{1990}; Surface{2012}; Surface{2034}; Surface{2056}; Surface{2078}; Surface{2100}; Surface{2122}; Surface{2144}; Surface{2166}; Surface{2188}; Surface{2210}; Surface{2232}; Surface{2254};
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
 Surface{2276};Surface{2298}; Surface{2320}; Surface{2342}; Surface{2364}; Surface{2386}; Surface{2408}; Surface{2430}; Surface{2452}; Surface{2474}; Surface{2496}; Surface{2518}; Surface{2540}; Surface{2562}; Surface{2584}; Surface{2606}; Surface{2628}; Surface{2650}; Surface{2672}; Surface{2694}; Surface{2716}; Surface{2738}; Surface{2760}; Surface{2782}; Surface{2804}; Surface{2826}; Surface{2848}; Surface{2870}; Surface{2892}; Surface{2914}; Surface{2936}; Surface{2958}; Surface{2980}; Surface{3002}; Surface{3024}; Surface{3046}; Surface{3068}; Surface{3090}; Surface{3112}; Surface{3134}; Surface{3156}; Surface{3178}; Surface{3200}; Surface{3222}; Surface{3244}; Surface{3266}; Surface{3288}; Surface{3310}; Surface{3332}; Surface{3354}; Surface{3376}; Surface{3398}; Surface{3420}; Surface{3442}; Surface{3464}; Surface{3486}; Surface{3508}; Surface{3530}; Surface{3552}; Surface{3574}; Surface{3596}; Surface{3618}; Surface{3640}; Surface{3662}; Surface{3684}; Surface{3706}; Surface{3728}; Surface{3750}; Surface{3772}; Surface{3794}; Surface{3816}; Surface{3838}; Surface{3860}; Surface{3882}; Surface{3904}; Surface{3926}; Surface{3948}; Surface{3970}; Surface{3992}; Surface{4014}; Surface{4036}; Surface{4058}; Surface{4080}; Surface{4102}; Surface{4124}; Surface{4146}; Surface{4168}; Surface{4190};
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{4212};Surface{4234}; Surface{4256}; Surface{4278}; Surface{4300}; Surface{4322}; Surface{4344}; Surface{4366}; Surface{4388}; Surface{4410}; Surface{4432}; Surface{4454}; Surface{4476}; Surface{4498}; Surface{4520}; Surface{4542}; Surface{4564}; Surface{4586}; Surface{4608}; Surface{4630}; Surface{4652}; Surface{4674}; Surface{4696}; Surface{4718}; Surface{4740}; Surface{4762}; Surface{4784}; Surface{4806}; Surface{4828}; Surface{4850}; Surface{4872}; Surface{4894}; Surface{4916}; Surface{4938}; Surface{4960}; Surface{4982}; Surface{5004}; Surface{5026}; Surface{5048}; Surface{5070}; Surface{5092}; Surface{5114}; Surface{5136}; Surface{5158}; Surface{5180}; Surface{5202}; Surface{5224}; Surface{5246}; Surface{5268}; Surface{5290}; Surface{5312}; Surface{5334}; Surface{5356}; Surface{5378}; Surface{5400}; Surface{5422}; Surface{5444}; Surface{5466}; Surface{5488}; Surface{5510}; Surface{5532}; Surface{5554}; Surface{5576}; Surface{5598}; Surface{5620}; Surface{5642}; Surface{5664}; Surface{5686}; Surface{5708}; Surface{5730}; Surface{5752}; Surface{5774}; Surface{5796}; Surface{5818}; Surface{5840}; Surface{5862}; Surface{5884}; Surface{5906}; Surface{5928}; Surface{5950}; Surface{5972}; Surface{5994}; Surface{6016}; Surface{6038}; Surface{6060}; Surface{6082}; Surface{6104}; Surface{6126}; 
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{6148};Surface{6170}; Surface{6192}; Surface{6214}; Surface{6236}; Surface{6258}; Surface{6280}; Surface{6302}; Surface{6324}; Surface{6346}; Surface{6368}; Surface{6390}; Surface{6412}; Surface{6434}; Surface{6456}; Surface{6478}; Surface{6500}; Surface{6522}; Surface{6544}; Surface{6566}; Surface{6588}; Surface{6610}; Surface{6632}; Surface{6654}; Surface{6676}; Surface{6698}; Surface{6720}; Surface{6742}; Surface{6764}; Surface{6786}; Surface{6808}; Surface{6830}; Surface{6852}; Surface{6874}; Surface{6896}; Surface{6918}; Surface{6940}; Surface{6962}; Surface{6984}; Surface{7006}; Surface{7028}; Surface{7050}; Surface{7072}; Surface{7094}; Surface{7116}; Surface{7138}; Surface{7160}; Surface{7182}; Surface{7204}; Surface{7226}; Surface{7248}; Surface{7270}; Surface{7292}; Surface{7314}; Surface{7336}; Surface{7358}; Surface{7380}; Surface{7402}; Surface{7424}; Surface{7446}; Surface{7468}; Surface{7490}; Surface{7512}; Surface{7534}; Surface{7556}; Surface{7578}; Surface{7600}; Surface{7622}; Surface{7644}; Surface{7666}; Surface{7688}; Surface{7710}; Surface{7732}; Surface{7754}; Surface{7776}; Surface{7798}; Surface{7820}; Surface{7842}; Surface{7864}; Surface{7886}; Surface{7908}; Surface{7930}; Surface{7952}; Surface{7974}; Surface{7996}; Surface{8018}; Surface{8040}; Surface{8062}; 
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{8084};Surface{8106}; Surface{8128}; Surface{8150}; Surface{8172}; Surface{8194}; Surface{8216}; Surface{8238}; Surface{8260}; Surface{8282}; Surface{8304}; Surface{8326}; Surface{8348}; Surface{8370}; Surface{8392}; Surface{8414}; Surface{8436}; Surface{8458}; Surface{8480}; Surface{8502}; Surface{8524}; Surface{8546}; Surface{8568}; Surface{8590}; Surface{8612}; Surface{8634}; Surface{8656}; Surface{8678}; Surface{8700}; Surface{8722}; Surface{8744}; Surface{8766}; Surface{8788}; Surface{8810}; Surface{8832}; Surface{8854}; Surface{8876}; Surface{8898}; Surface{8920}; Surface{8942}; Surface{8964}; Surface{8986}; Surface{9008}; Surface{9030}; Surface{9052}; Surface{9074}; Surface{9096}; Surface{9118}; Surface{9140}; Surface{9162}; Surface{9184}; Surface{9206}; Surface{9228}; Surface{9250}; Surface{9272}; Surface{9294}; Surface{9316}; Surface{9338}; Surface{9360}; Surface{9382}; Surface{9404}; Surface{9426}; Surface{9448}; Surface{9470}; Surface{9492}; Surface{9514}; Surface{9536}; Surface{9558}; Surface{9580}; Surface{9602}; Surface{9624}; Surface{9646}; Surface{9668}; Surface{9690}; Surface{9712}; Surface{9734}; Surface{9756}; Surface{9778}; Surface{9800}; Surface{9822}; Surface{9844}; Surface{9866}; Surface{9888}; Surface{9910}; Surface{9932}; Surface{9954}; Surface{9976}; Surface{9998}; 
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{10020};Surface{10042}; Surface{10064}; Surface{10086}; Surface{10108}; Surface{10130}; Surface{10152}; Surface{10174}; Surface{10196}; Surface{10218}; Surface{10240}; Surface{10262}; Surface{10284}; Surface{10306}; Surface{10328}; Surface{10350}; Surface{10372}; Surface{10394}; Surface{10416}; Surface{10438}; Surface{10460}; Surface{10482}; Surface{10504}; Surface{10526}; Surface{10548}; Surface{10570}; Surface{10592}; Surface{10614}; Surface{10636}; Surface{10658}; Surface{10680}; Surface{10702}; Surface{10724}; Surface{10746}; Surface{10768}; Surface{10790}; Surface{10812}; Surface{10834}; Surface{10856}; Surface{10878}; Surface{10900}; Surface{10922}; Surface{10944}; Surface{10966}; Surface{10988}; Surface{11010}; Surface{11032}; Surface{11054}; Surface{11076}; Surface{11098}; Surface{11120}; Surface{11142}; Surface{11164}; Surface{11186}; Surface{11208}; Surface{11230}; Surface{11252}; Surface{11274}; Surface{11296}; Surface{11318}; Surface{11340}; Surface{11362}; Surface{11384}; Surface{11406}; Surface{11428}; Surface{11450}; Surface{11472}; Surface{11494}; Surface{11516}; Surface{11538}; Surface{11560}; Surface{11582}; Surface{11604}; Surface{11626}; Surface{11648}; Surface{11670}; Surface{11692}; Surface{11714}; Surface{11736}; Surface{11758}; Surface{11780}; Surface{11802}; Surface{11824}; Surface{11846}; Surface{11868}; Surface{11890}; Surface{11912}; Surface{11934};
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{11956};Surface{11978}; Surface{12000}; Surface{12022}; Surface{12044}; Surface{12066}; Surface{12088}; Surface{12110}; Surface{12132}; Surface{12154}; Surface{12176}; Surface{12198}; Surface{12220}; Surface{12242}; Surface{12264}; Surface{12286}; Surface{12308}; Surface{12330}; Surface{12352}; Surface{12374}; Surface{12396}; Surface{12418}; Surface{12440}; Surface{12462}; Surface{12484}; Surface{12506}; Surface{12528}; Surface{12550}; Surface{12572}; Surface{12594}; Surface{12616}; Surface{12638}; Surface{12660}; Surface{12682}; Surface{12704}; Surface{12726}; Surface{12748}; Surface{12770}; Surface{12792}; Surface{12814}; Surface{12836}; Surface{12858}; Surface{12880}; Surface{12902}; Surface{12924}; Surface{12946}; Surface{12968}; Surface{12990}; Surface{13012}; Surface{13034}; Surface{13056}; Surface{13078}; Surface{13100}; Surface{13122}; Surface{13144}; Surface{13166}; Surface{13188}; Surface{13210}; Surface{13232}; Surface{13254}; Surface{13276}; Surface{13298}; Surface{13320}; Surface{13342}; Surface{13364}; Surface{13386}; Surface{13408}; Surface{13430}; Surface{13452}; Surface{13474}; Surface{13496}; Surface{13518}; Surface{13540}; Surface{13562}; Surface{13584}; Surface{13606}; Surface{13628}; Surface{13650}; Surface{13672}; Surface{13694}; Surface{13716}; Surface{13738}; Surface{13760}; Surface{13782}; Surface{13804}; Surface{13826}; Surface{13848}; Surface{13870}; 
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{13892};Surface{13914}; Surface{13936}; Surface{13958}; Surface{13980}; Surface{14002}; Surface{14024}; Surface{14046}; Surface{14068}; Surface{14090}; Surface{14112}; Surface{14134}; Surface{14156}; Surface{14178}; Surface{14200}; Surface{14222}; Surface{14244}; Surface{14266}; Surface{14288}; Surface{14310}; Surface{14332}; Surface{14354}; Surface{14376}; Surface{14398}; Surface{14420}; Surface{14442}; Surface{14464}; Surface{14486}; Surface{14508}; Surface{14530}; Surface{14552}; Surface{14574}; Surface{14596}; Surface{14618}; Surface{14640}; Surface{14662}; Surface{14684}; Surface{14706}; Surface{14728}; Surface{14750}; Surface{14772}; Surface{14794}; Surface{14816}; Surface{14838}; Surface{14860}; Surface{14882}; Surface{14904}; Surface{14926}; Surface{14948}; Surface{14970}; Surface{14992}; Surface{15014}; Surface{15036}; Surface{15058}; Surface{15080}; Surface{15102}; Surface{15124}; Surface{15146}; Surface{15168}; Surface{15190}; Surface{15212}; Surface{15234}; Surface{15256}; Surface{15278}; Surface{15300}; Surface{15322}; Surface{15344}; Surface{15366}; Surface{15388}; Surface{15410}; Surface{15432}; Surface{15454}; Surface{15476}; Surface{15498}; Surface{15520}; Surface{15542}; Surface{15564}; Surface{15586}; Surface{15608}; Surface{15630}; Surface{15652}; Surface{15674}; Surface{15696}; Surface{15718}; Surface{15740}; Surface{15762}; Surface{15784}; Surface{15806}; 
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{15828};Surface{15850}; Surface{15872}; Surface{15894}; Surface{15916}; Surface{15938}; Surface{15960}; Surface{15982}; Surface{16004}; Surface{16026}; Surface{16048}; Surface{16070}; Surface{16092}; Surface{16114}; Surface{16136}; Surface{16158}; Surface{16180}; Surface{16202}; Surface{16224}; Surface{16246}; Surface{16268}; Surface{16290}; Surface{16312}; Surface{16334}; Surface{16356}; Surface{16378}; Surface{16400}; Surface{16422}; Surface{16444}; Surface{16466}; Surface{16488}; Surface{16510}; Surface{16532}; Surface{16554}; Surface{16576}; Surface{16598}; Surface{16620}; Surface{16642}; Surface{16664}; Surface{16686}; Surface{16708}; Surface{16730}; Surface{16752}; Surface{16774}; Surface{16796}; Surface{16818}; Surface{16840}; Surface{16862}; Surface{16884}; Surface{16906}; Surface{16928}; Surface{16950}; Surface{16972}; Surface{16994}; Surface{17016}; Surface{17038}; Surface{17060}; Surface{17082}; Surface{17104}; Surface{17126}; Surface{17148}; Surface{17170}; Surface{17192}; Surface{17214}; Surface{17236}; Surface{17258}; Surface{17280}; Surface{17302}; Surface{17324}; Surface{17346}; Surface{17368}; Surface{17390}; Surface{17412}; Surface{17434}; Surface{17456}; Surface{17478}; Surface{17500}; Surface{17522}; Surface{17544}; Surface{17566}; Surface{17588}; Surface{17610}; Surface{17632}; Surface{17654}; Surface{17676}; Surface{17698}; Surface{17720}; Surface{17742};
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{17764};Surface{17786}; Surface{17808}; Surface{17830}; Surface{17852}; Surface{17874}; Surface{17896}; Surface{17918}; Surface{17940}; Surface{17962}; Surface{17984}; Surface{18006}; Surface{18028}; Surface{18050}; Surface{18072}; Surface{18094}; Surface{18116}; Surface{18138}; Surface{18160}; Surface{18182}; Surface{18204}; Surface{18226}; Surface{18248}; Surface{18270}; Surface{18292}; Surface{18314}; Surface{18336}; Surface{18358}; Surface{18380}; Surface{18402}; Surface{18424}; Surface{18446}; Surface{18468}; Surface{18490}; Surface{18512}; Surface{18534}; Surface{18556}; Surface{18578}; Surface{18600}; Surface{18622}; Surface{18644}; Surface{18666}; Surface{18688}; Surface{18710}; Surface{18732}; Surface{18754}; Surface{18776}; Surface{18798}; Surface{18820}; Surface{18842}; Surface{18864}; Surface{18886}; Surface{18908}; Surface{18930}; Surface{18952}; Surface{18974}; Surface{18996}; Surface{19018}; Surface{19040}; Surface{19062}; Surface{19084}; Surface{19106}; Surface{19128}; Surface{19150}; Surface{19172}; Surface{19194}; Surface{19216}; Surface{19238}; Surface{19260}; Surface{19282}; Surface{19304}; Surface{19326}; Surface{19348}; Surface{19370}; Surface{19392}; Surface{19414}; Surface{19436}; Surface{19458}; Surface{19480}; Surface{19502}; Surface{19524}; Surface{19546}; Surface{19568}; Surface{19590}; Surface{19612}; Surface{19634}; Surface{19656}; Surface{19678}; 
 Layers{nr}; Recombine;
}

Extrude {{0, 0, 1}, {0, 0, 0}, Pi/6} {
Surface{19700};Surface{19722}; Surface{19744}; Surface{19766}; Surface{19788}; Surface{19810}; Surface{19832}; Surface{19854}; Surface{19876}; Surface{19898}; Surface{19920}; Surface{19942}; Surface{19964}; Surface{19986}; Surface{20008}; Surface{20030}; Surface{20052}; Surface{20074}; Surface{20096}; Surface{20118}; Surface{20140}; Surface{20162}; Surface{20184}; Surface{20206}; Surface{20228}; Surface{20250}; Surface{20272}; Surface{20294}; Surface{20316}; Surface{20338}; Surface{20360}; Surface{20382}; Surface{20404}; Surface{20426}; Surface{20448}; Surface{20470}; Surface{20492}; Surface{20514}; Surface{20536}; Surface{20558}; Surface{20580}; Surface{20602}; Surface{20624}; Surface{20646}; Surface{20668}; Surface{20690}; Surface{20712}; Surface{20734}; Surface{20756}; Surface{20778}; Surface{20800}; Surface{20822}; Surface{20844}; Surface{20866}; Surface{20888}; Surface{20910}; Surface{20932}; Surface{20954}; Surface{20976}; Surface{20998}; Surface{21020}; Surface{21042}; Surface{21064}; Surface{21086}; Surface{21108}; Surface{21130}; Surface{21152}; Surface{21174}; Surface{21196}; Surface{21218}; Surface{21240}; Surface{21262}; Surface{21284}; Surface{21306}; Surface{21328}; Surface{21350}; Surface{21372}; Surface{21394}; Surface{21416}; Surface{21438}; Surface{21460}; Surface{21482}; Surface{21504}; Surface{21526}; Surface{21548}; Surface{21570}; Surface{21592}; Surface{21614};
 Layers{nr}; Recombine;
}

//+
Physical Surface("baffles", 4191) = {4, 8, 23, 24, 295, 128, 133, 299, 207, 212, 303, 286, 291, 307};
//+
Physical Surface("blades", 23183) = {12, 16, 17, 13, 78, 93, 83, 98, 157, 172, 177, 162, 236, 251, 256, 241};
//+
Physical Surface("blades", 23183) += {2518, 2606, 2628, 2540, 3002, 3024, 3046, 2980, 3486, 3508, 3398, 3420, 3926, 3948, 3860, 3838};
//+
Physical Surface("baffles", 4191) += {6126, 6038, 6016, 5686, 5598, 5576, 5180, 5158, 5136, 4806, 4718, 4696, 4366, 4278};
//+
Physical Surface("blades", 23183) += {7820, 7732, 7710, 7798, 7380, 7270, 7292, 7358, 6852, 6918, 6874, 6896, 6500, 6478, 6390, 6412};
//+
//+
Physical Surface("baffles", 4191) += {11934, 11846, 11824, 11494, 11406, 11384, 10988, 10966, 10944, 10614, 10526, 10504, 10174, 10086};
//+
Physical Surface("blades", 23183) += {10262, 10350, 10372, 10284, 10746, 10768, 10790, 10724, 11164, 11142, 11252, 11230, 11582, 11604, 11692, 11670};
//+
Physical Surface("blades", 23183) += {15454, 15476, 15564, 15542, 15036, 15014, 15124, 15102, 14618, 14640, 14662, 14596, 14134, 14156, 14244, 14222};
//+
Physical Surface("baffles", 4191) += {17742, 17654, 17632, 17302, 17214, 17192, 16796, 16774, 16752, 16422, 16334, 16312, 15982, 15894};
//+
Physical Surface("blades", 23183) += {19326, 19348, 19436, 19414, 18908, 18886, 18996, 18974, 18490, 18468, 18534, 18512, 18006, 18028, 18116, 18094};
//+
Physical Surface("internalToMerge3", 23184) = {327, 2263, 4199, 6135, 8071, 10007, 11943, 13879, 15815, 17751, 19687, 21623};
//+
Physical Surface("rod", 23185) = {415, 855, 1361, 1735, 2175, 2351, 2791, 3297, 3671, 4111, 4287, 4727, 5233, 5607, 6047, 6223, 6663, 7169, 7543, 7983, 8159, 8599, 9105, 9479, 9919, 10095, 10535, 11041, 11415, 11855, 12031, 12471, 12977, 13351, 13791, 13967, 14407, 14913, 15287, 15727, 15903, 16343, 16849, 17223, 17663, 17839, 18279, 18785, 19159, 19599, 19775, 20215, 20721, 21095, 21535, 21707, 22059, 22462, 22767, 23123};
//+
Physical Surface("rodRotatingZone", 23186) = {503, 525, 965, 987, 1383, 1405, 1823, 1845, 2439, 2461, 2901, 2923, 3319, 3341, 3759, 3781, 4375, 4397, 4837, 4859, 5255, 5277, 5695, 5717, 6311, 6333, 6773, 6795, 7191, 7213, 7631, 7653, 8247, 8269, 8709, 8731, 9127, 9149, 9567, 9589, 10183, 10205, 10645, 10667, 11063, 11085, 11503, 11525, 12119, 12141, 12581, 12603, 12999, 13021, 13439, 13461, 14055, 14077, 14517, 14539, 14935, 14957, 15375, 15397, 15991, 16013, 16453, 16475, 16871, 16893, 17311, 17333, 17927, 17949, 18389, 18411, 18807, 18829, 19247, 19269, 19863, 19885, 20325, 20347, 20743, 20765, 21183, 21205, 22856, 22835, 22496, 22475, 22161, 22144, 21796, 21775};
//+
Physical Surface("dishes", 23187) = {507, 573, 969, 1043, 1387, 1461, 1827, 1893, 2443, 2509, 2905, 2979, 3323, 3397, 3763, 3829, 4379, 4445, 4841, 4915, 5259, 5333, 5699, 5765, 6315, 6381, 6777, 6851, 7195, 7269, 7635, 7701, 8251, 8317, 8713, 8787, 9131, 9205, 9571, 9637, 10187, 10253, 10649, 10723, 11067, 11141, 11507, 11573, 12123, 12189, 12585, 12659, 13003, 13077, 13443, 13509, 14059, 14125, 14521, 14595, 14939, 15013, 15379, 15445, 15995, 16061, 16457, 16531, 16875, 16949, 17315, 17381, 17931, 17997, 18393, 18467, 18811, 18885, 19251, 19317, 19867, 19933, 20329, 20403, 20747, 20821, 21187, 21253, 22479, 22546, 22148, 22211, 21779, 21834, 22839, 22898};
//+
Physical Surface("wall", 23188) = {2249, 2161, 2139, 1809, 1721, 1699, 1303, 1281, 1259, 929, 841, 819, 489, 401, 4185, 4097, 4075, 3745, 3657, 3635, 3239, 3217, 3195, 2865, 2777, 2755, 2425, 2337, 6121, 6033, 6011, 5681, 5593, 5571, 5175, 5153, 5131, 4801, 4713, 4691, 4361, 4273, 8057, 7969, 7947, 7617, 7529, 7507, 7111, 7089, 7067, 6737, 6649, 6627, 6297, 6209, 9993, 9905, 9883, 9553, 9465, 9443, 9047, 9025, 9003, 8673, 8585, 8563, 8233, 8145, 11929, 11841, 11819, 11489, 11401, 11379, 10983, 10961, 10939, 10609, 10521, 10499, 10169, 10081, 13865, 13777, 13755, 13425, 13337, 13315, 12919, 12897, 12875, 12545, 12457, 12435, 12105, 12017, 15801, 15713, 15691, 15361, 15273, 15251, 14855, 14833, 14811, 14481, 14393, 14371, 14041, 13953, 17737, 17649, 17627, 17297, 17209, 17187, 16791, 16769, 16747, 16417, 16329, 16307, 15977, 15889, 19673, 19585, 19563, 19233, 19145, 19123, 18727, 18705, 18683, 18353, 18265, 18243, 17913, 17825, 21609, 21521, 21499, 21169, 21081, 21059, 20663, 20641, 20619, 20289, 20201, 20179, 19849, 19761, 23182, 23114, 23097, 22826, 22758, 22741, 22427, 22410, 22393, 22118, 22050, 22033, 21766, 21694};
//+
Physical Surface("top", 23189) = {2245, 2223, 2201, 2179, 4181, 4159, 4137, 4115, 6117, 6095, 6073, 6051, 8053, 8031, 8009, 7987, 9989, 9967, 9945, 9923, 11925, 11903, 11881, 11859, 13861, 13839, 13817, 13795, 15797, 15775, 15753, 15731, 17733, 17711, 17689, 17667, 19669, 19647, 19625, 19603, 21605, 21583, 21561, 21539, 23127, 23144, 23161, 23178};
//+
Physical Surface("internalToMerge2", 23190) = {405, 383, 361, 339, 2341, 2319, 2297, 2275, 4277, 4255, 4233, 4211, 6213, 6191, 6169, 6147, 8149, 8127, 8105, 8083, 10085, 10063, 10041, 10019, 12021, 11999, 11977, 11955, 13957, 13935, 13913, 13891, 15893, 15871, 15849, 15827, 17829, 17807, 17785, 17763, 19765, 19743, 19721, 19699, 21635, 21656, 21677, 21698};
//+
Physical Volume("tank", 23191) = {1, 2, 3, 4, 5, 6, 7, 8, 21, 23, 22, 24, 25, 26, 27, 28, 42, 43, 41, 44, 48, 47, 46, 45, 61, 63, 62, 64, 65, 66, 67, 68, 81, 83, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 109, 111, 110, 112, 113, 114, 115, 116, 130, 131, 129, 132, 136, 135, 134, 133, 149, 151, 150, 152, 153, 154, 155, 156, 169, 171, 170, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 197, 199, 198, 200, 201, 202, 203, 204, 218, 219, 217, 220, 224, 223, 222, 221, 237, 239, 238, 240, 241, 242, 243, 244, 257, 259, 258, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 285, 287, 286, 288, 289, 290, 291, 292, 306, 307, 305, 308, 312, 311, 310, 309, 325, 327, 326, 328, 329, 330, 331, 332, 345, 347, 346, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 373, 375, 374, 376, 377, 378, 379, 380, 394, 395, 393, 396, 400, 399, 398, 397, 413, 415, 414, 416, 417, 418, 419, 420, 433, 435, 434, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 461, 463, 462, 464, 465, 466, 467, 468, 482, 483, 481, 484, 488, 487, 486, 485, 501, 503, 502, 504, 505, 506, 507, 508, 521, 523, 522, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 549, 551, 550, 552, 553, 554, 555, 556, 570, 571, 569, 572, 576, 575, 574, 573, 589, 591, 590, 592, 593, 594, 595, 596, 609, 611, 610, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 637, 639, 638, 640, 641, 642, 643, 644, 658, 659, 657, 660, 664, 663, 662, 661, 677, 679, 678, 680, 681, 682, 683, 684, 697, 699, 698, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 725, 727, 726, 728, 729, 730, 731, 732, 746, 747, 745, 748, 752, 751, 750, 749, 765, 767, 766, 768, 769, 770, 771, 772, 785, 787, 786, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 813, 815, 814, 816, 817, 818, 819, 820, 834, 835, 833, 836, 840, 839, 838, 837, 853, 855, 854, 856, 857, 858, 859, 860, 873, 875, 874, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 901, 903, 902, 904, 905, 906, 907, 908, 922, 923, 921, 924, 928, 927, 926, 925, 941, 943, 942, 944, 945, 946, 947, 948, 961, 963, 962, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 989, 991, 990, 992, 993, 994, 995, 996, 1010, 1011, 1009, 1012, 1016, 1015, 1014, 1013, 1029, 1031, 1030, 1032, 1033, 1034, 1035, 1036, 1049, 1051, 1050, 1052, 1053, 1054, 1055, 1056};
//+
Physical Volume("rotatingZone", 23192) = {11, 9, 12, 15, 19, 16, 13, 17, 20, 18, 14, 10, 30, 29, 31, 32, 33, 34, 36, 35, 38, 39, 40, 37, 49, 54, 53, 50, 51, 52, 57, 56, 55, 60, 59, 58, 69, 74, 72, 75, 79, 76, 73, 70, 71, 77, 78, 80, 99, 97, 100, 103, 107, 104, 101, 105, 108, 106, 102, 98, 118, 117, 119, 120, 121, 122, 124, 123, 126, 127, 128, 125, 137, 142, 141, 138, 139, 140, 145, 144, 143, 148, 147, 146, 157, 162, 160, 163, 167, 164, 161, 158, 159, 165, 166, 168, 187, 185, 188, 191, 195, 192, 189, 193, 196, 194, 190, 186, 206, 205, 207, 208, 209, 210, 212, 211, 214, 215, 216, 213, 225, 230, 229, 226, 227, 228, 233, 232, 231, 236, 235, 234, 245, 250, 248, 251, 255, 252, 249, 246, 247, 253, 254, 256, 275, 273, 276, 279, 283, 280, 277, 281, 284, 282, 278, 274, 294, 293, 295, 296, 297, 298, 300, 299, 302, 303, 304, 301, 313, 318, 317, 314, 315, 316, 321, 320, 319, 324, 323, 322, 333, 338, 336, 339, 343, 340, 337, 334, 335, 341, 342, 344, 363, 361, 364, 367, 371, 368, 365, 369, 372, 370, 366, 362, 382, 381, 383, 384, 385, 386, 388, 387, 390, 391, 392, 389, 401, 406, 405, 402, 403, 404, 409, 408, 407, 412, 411, 410, 421, 426, 424, 427, 431, 428, 425, 422, 423, 429, 430, 432, 451, 449, 452, 455, 459, 456, 453, 457, 460, 458, 454, 450, 470, 469, 471, 472, 473, 474, 476, 475, 478, 479, 480, 477, 489, 494, 493, 490, 491, 492, 497, 496, 495, 500, 499, 498, 509, 514, 512, 515, 519, 516, 513, 510, 511, 517, 518, 520, 539, 537, 540, 543, 547, 544, 541, 545, 548, 546, 542, 538, 558, 557, 559, 560, 561, 562, 564, 563, 566, 567, 568, 565, 577, 582, 581, 578, 579, 580, 585, 584, 583, 588, 587, 586, 597, 602, 600, 603, 607, 604, 601, 598, 599, 605, 606, 608, 627, 625, 628, 631, 635, 632, 629, 633, 636, 634, 630, 626, 646, 645, 647, 648, 649, 650, 652, 651, 654, 655, 656, 653, 665, 670, 669, 666, 667, 668, 673, 672, 671, 676, 675, 674, 685, 690, 688, 691, 695, 692, 689, 686, 687, 693, 694, 696, 715, 713, 716, 719, 723, 720, 717, 721, 724, 722, 718, 714, 734, 733, 735, 736, 737, 738, 740, 739, 742, 743, 744, 741, 753, 758, 757, 754, 755, 756, 761, 760, 759, 764, 763, 762, 773, 778, 776, 779, 783, 780, 777, 774, 775, 781, 782, 784, 803, 801, 804, 807, 811, 808, 805, 809, 812, 810, 806, 802, 822, 821, 823, 824, 825, 826, 828, 827, 830, 831, 832, 829, 841, 846, 845, 842, 843, 844, 849, 848, 847, 852, 851, 850, 861, 866, 864, 867, 871, 868, 865, 862, 863, 869, 870, 872, 891, 889, 892, 895, 899, 896, 893, 897, 900, 898, 894, 890, 910, 909, 911, 912, 913, 914, 916, 915, 918, 919, 920, 917, 929, 934, 933, 930, 931, 932, 937, 936, 935, 940, 939, 938, 949, 954, 952, 955, 959, 956, 953, 950, 951, 957, 958, 960, 979, 977, 980, 983, 987, 984, 981, 985, 988, 986, 982, 978, 998, 997, 999, 1000, 1001, 1002, 1004, 1003, 1006, 1007, 1008, 1005, 1017, 1022, 1021, 1018, 1019, 1020, 1025, 1024, 1023, 1028, 1027, 1026, 1037, 1042, 1040, 1043, 1047, 1044, 1041, 1038, 1039, 1045, 1046, 1048};
