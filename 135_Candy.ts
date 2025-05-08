function candy(ratings: number[]) {
  const size=ratings.length
  const ans=new Array(size).fill(1);
  for (let i=1;i<size;i++)
    if (ratings[i]>ratings[i-1])
      ans[i]=ans[i-1]+1
  for (let i=size-2;i>=0;i--)
    if (ratings[i]>ratings[i+1])
      ans[i]=ans[i+1]+1
  return ans.reduce((a,b)=>a+b,0)
}
const ans=candy([1,0,2])
console.log(ans)