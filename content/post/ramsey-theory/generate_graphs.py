"""ラムゼー理論の記事用図と全列挙データ。依存: matplotlib。"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parent
RED, BLUE = '#dc3545', '#087fc0'

def enumerate_colorings(n):
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triangle_masks = [sum(1 << edge_index[edge] for edge in combinations(vertices, 2))
                      for vertices in combinations(range(n), 3)]
    histogram = Counter()
    for coloring in range(1 << len(edges)):
        count = sum((coloring & mask) in (0, mask) for mask in triangle_masks)
        histogram[count] += 1
    total = 1 << len(edges)
    return dict(n=n, edges=len(edges), total=total, without_triangle=histogram[0],
                with_triangle=total-histogram[0], probability=1-histogram[0]/total,
                minimum=min(histogram), expected=sum(k*v for k,v in histogram.items())/total,
                histogram=dict(sorted(histogram.items())))

def finish(fig, name):
    path = ROOT / name
    fig.savefig(path, bbox_inches='tight', pad_inches=.3)
    path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)

def network(ax, positions, colors, title, highlight=()):
    for edge, color in colors.items():
        a,b=edge
        xs,ys=zip(positions[a],positions[b])
        ax.plot(xs,ys,color=color,lw=3.5 if edge in highlight else 2,
                linestyle='--' if color==BLUE else '-',alpha=.95,zorder=1)
    for name,(x,y) in positions.items():
        ax.scatter(x,y,s=500,color='#182b49',zorder=3)
        ax.text(x,y,name,color='white',fontsize=14,ha='center',va='center',zorder=4)
    ax.set_title(title,pad=18,fontsize=13)
    ax.set_aspect('equal');ax.axis('off');ax.margins(.2)

def main():
    plt.rcParams.update({'font.family':['Meiryo','DejaVu Sans'],'font.size':12,
                         'svg.fonttype':'none','figure.facecolor':'#f8fafc',
                         'axes.facecolor':'#f8fafc','axes.spines.top':False,'axes.spines.right':False})
    results=[enumerate_colorings(n) for n in range(3,7)]
    data={'model':'各辺を独立に確率1/2で赤または青にする。頂点にはラベルがある。',
          'enumeration':results,'sequence':[4,1,5,2,6,3], 'increasing_indices':[2,4,6]}
    (ROOT/'calculation-results.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    pos={'A':(0,1.1),'B':(-.9,-.45),'C':(0,-1.15),'D':(.9,-.45),'E':(-1.05,.7),'F':(1.05,.7)}
    base={('A',x):RED for x in 'BCD'}
    base.update({('A','E'):'#bac2cd',('A','F'):'#bac2cd'})
    fig,axs=plt.subplots(1,3,figsize=(15,5))
    network(axs[0],pos,base,'① Aから出る5本のうち\n同じ色が少なくとも3本')
    first={**base,('B','C'):RED}
    network(axs[1],pos,first,'② B・C・Dの間に赤がある\nAを含む赤い三角形',highlight=(('A','B'),('A','C'),('B','C')))
    second={**base,('B','C'):BLUE,('B','D'):BLUE,('C','D'):BLUE}
    network(axs[2],pos,second,'③ B・C・Dの間に赤がない\nB・C・Dが青い三角形',highlight=(('B','C'),('B','D'),('C','D')))
    fig.text(.5,.04,'赤：実線　青：破線　灰色・省略した辺：証明では色を問わない',ha='center',fontsize=12)
    fig.subplots_adjust(bottom=.17,wspace=.25)
    finish(fig,'six-person-proof.svg')

    names='ABCDE'
    pentagon={name:(math.cos(math.pi/2+2*math.pi*i/5),math.sin(math.pi/2+2*math.pi*i/5)) for i,name in enumerate(names)}
    red_edges={tuple(sorted((names[i],names[(i+1)%5]))) for i in range(5)}
    colors={edge:RED if edge in red_edges else BLUE for edge in combinations(names,2)}
    for tri in combinations(names,3):
        assert len({colors[e] for e in combinations(tri,2)})==2
    fig,ax=plt.subplots(figsize=(8,7))
    network(ax,pentagon,colors,'5人なら、単色の三角形を避けられる')
    fig.legend(handles=[Line2D([0],[0],color=RED,lw=3,label='赤：五角形の外周'),Line2D([0],[0],color=BLUE,lw=3,ls='--',label='青：五角形の対角線')],loc='lower center',ncol=2,frameon=False)
    finish(fig,'five-person-counterexample.svg')

    fig,ax=plt.subplots(figsize=(10,6))
    bars=ax.bar([r['n'] for r in results],[r['probability']*100 for r in results],color=['#94a3b8']*3+['#087fc0'],width=.6)
    for bar,r in zip(bars,results):
        ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+2,f"{r['probability']*100:.2f}%\n{r['with_triangle']}/{r['total']}",ha='center',fontsize=12)
    ax.set(xticks=[3,4,5,6],ylim=(0,120),yticks=[0,25,50,75,100],xlabel='人数（頂点の数）',ylabel='単色の三角形がある色分けの割合（%）',title='5人では「ほぼ必ず」、6人では例外なく「必ず」')
    ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
    finish(fig,'coloring-probability.svg')

    values=data['sequence'];xs=list(range(1,7))
    fig,ax=plt.subplots(figsize=(10,5))
    ax.scatter(xs,values,s=110,color='#64748b',zorder=3,label='元の数列')
    ax.plot([2,4,6],[1,2,3],color=RED,lw=3,marker='o',ms=10,label='増加する部分列：1 → 2 → 3')
    for x,y in zip(xs,values):ax.annotate(str(y),(x,y),xytext=(0,12),textcoords='offset points',ha='center')
    ax.set(xticks=xs,yticks=xs,ylim=(.5,7.2),xlabel='元の数列での位置',ylabel='値',title='飛び飛びに選んでも、元の順番は変えない')
    ax.legend(loc='upper left',fontsize=11);ax.grid(alpha=.2)
    finish(fig,'monotone-subsequence.svg')
    for r in results:print(r)

if __name__=='__main__':main()
