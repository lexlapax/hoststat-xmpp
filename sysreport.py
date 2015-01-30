from linux_metrics import cpu_stat

while True:
	cpu_pcts = cpu_stat.cpu_percents(5)
	print 'cpu utilization: %.2f%%' % (100 - cpu_pcts['idle'])
