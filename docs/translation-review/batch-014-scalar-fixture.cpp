// Append to the first four extracted C++ blocks; public test values only.

int main(){
 Point G(cpp_int("0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798"),cpp_int("0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8"));
 cpp_int values[] = {cpp_int("0"),cpp_int("1"),cpp_int("2"),cpp_int("3"),cpp_int("7"),cpp_int("42"),cpp_int("65537"),cpp_int("340282366920938463463374607431768211456"),cpp_int("57896044618658097711785492504343953926634992332820282019728792003956564819968"),cpp_int("115792089237316195423570985008687907853269984665640564039457584007913129639935"),cpp_int("115792089237316195423570985008687907852837564279074904382605163141518161494336"),cpp_int("115792089237316195423570985008687907852837564279074904382605163141518161494337"),cpp_int("115792089237316195423570985008687907852837564279074904382605163141518161494338")};
 int index=0;
 for (const auto& value:values) {
  Point out=scalarMultiply(G,value);
  std::cout<<std::dec<<index++<<":"<<out.isInfinity<<":"<<std::hex<<out.x<<":"<<out.y<<"\n";
 }
 int rejects=0;
 auto reject=[&](auto action){try{action();throw std::runtime_error("Expected invalid input rejection");}catch(const std::invalid_argument&){++rejects;}};
 reject([&]{mod(1,0);});reject([&]{mod(1,-1);});
 reject([&]{powerMod(2,-1,p);});reject([&]{powerMod(2,1,1);});
 reject([&]{modInverse(0);});reject([&]{modInverse(p);});
 reject([&]{scalarMultiply(G,-1);});reject([&]{scalarMultiply(G,cpp_int(1)<<256);});
 reject([&]{scalarMultiply(Point(0,0),1);});
 reject([&]{scalarMultiply(Point(G.x+p,G.y),1);});
 reject([&]{pointAdd(Point(0,0),G);});reject([&]{pointAdd(G,Point(0,0));});
 reject([&]{Point A=G,B;conditionalSwapDemo(A,B,2);});
 if (!scalarMultiply(Point(),42).isInfinity) throw std::runtime_error("Infinity input");
 if (mod(-1,p)!=p-1 || modInverse(-1)!=p-1 || mod(7*modInverse(7),p)!=1) throw std::runtime_error("Field fixtures");
 Point neg(G.x,mod(-G.y,p));
 if (!pointAdd(G,neg).isInfinity) throw std::runtime_error("Inverse point");
 Point l=G,r;conditionalSwapDemo(l,r,0);if(l.isInfinity || !r.isInfinity) throw std::runtime_error("Swap0");
 conditionalSwapDemo(l,r,1);if(!l.isInfinity || r.isInfinity) throw std::runtime_error("Swap1");
 std::cout<<std::dec<<"rejections="<<rejects<<"\n";
}
