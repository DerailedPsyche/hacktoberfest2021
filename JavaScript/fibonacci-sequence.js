var fibonacciSeries = (n) => {
	if (n === 1) {
		return [0, 1];
	} else {
		let s = fibonacciSeries(n - 1);
		s.push(s[s.length - 1] + s[s.length - 2]);
		return s;
	}
 };

console.log(fibonacciSeries(8));
