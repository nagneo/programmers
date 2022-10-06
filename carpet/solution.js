function solution (brown, yellow)
{
  // 이차 방정식을 이용하여 근의 공식으로 풀기
  const b = 0.5 * (brown + 4)
  const c = brown + yellow
  const width = 0.5 * (b + (b*b - 4*1*c) ** (1/2))
  const height = c / width

  return [width, height]
}