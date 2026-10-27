// Append to the common core with p=17, a=2, b=0; not a cryptographic curve.

#include <vector>
bool same(const Point& P,const Point& Q){return P.isInfinity==Q.isInfinity && (P.isInfinity || (P.x==Q.x && P.y==Q.y));}
int main(){
 std::vector<Point> points{Point()};
 for(int x=0;x<17;++x)for(int y=0;y<17;++y)if(isOnCurve(Point(x,y)))points.push_back(Point(x,y));
 std::size_t pairs=0,triples=0,scalars=0,zeroY=0;
 for(std::size_t i=0;i<points.size();++i){
  const Point& P=points[i];Point accum;
  if(!P.isInfinity && P.y==0){if(!pointAdd(P,P).isInfinity)throw std::runtime_error("y=0 doubling");++zeroY;}
  for(int k=0;k<=40;++k){if(!same(scalarMultiply(P,k),accum))throw std::runtime_error("Ladder vs repeated add");accum=pointAdd(accum,P);++scalars;}
  for(std::size_t j=0;j<points.size();++j){
   Point sum=pointAdd(P,points[j]);if(!isOnCurve(sum))throw std::runtime_error("Closure");
   std::cout<<"pair="<<i<<","<<j<<","<<sum.isInfinity<<","<<sum.x<<","<<sum.y<<"\n";++pairs;
   if(!same(sum,pointAdd(points[j],P)))throw std::runtime_error("Commutativity");
   for(const Point& R:points){if(!same(pointAdd(sum,R),pointAdd(P,pointAdd(points[j],R))))throw std::runtime_error("Associativity");++triples;}
  }
 }
 std::cout<<"counts="<<points.size()<<","<<pairs<<","<<triples<<","<<scalars<<","<<zeroY<<"\n";
}
