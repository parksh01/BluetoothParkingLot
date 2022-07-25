import matplotlib.pyplot as plt

loss = [0.4323543310165405, 0.05610208958387375, 0.0335516594350338, 0.024582773447036743, 0.01910238526761532, 0.015140140429139137, 0.01287159789353609, 0.010924645699560642, 0.009428657591342926, 0.00806695781648159, 0.006925018038600683, 0.00601628702133894, 0.0055242497473955154, 0.0046120909973979, 0.004006834700703621, 0.0037236749194562435, 0.0033132536336779594, 0.0028226824942976236, 0.002606806578114629, 0.0026624579913914204, 0.002333307173103094, 0.0019500552443787456, 0.0019165134290233254, 0.0015353822382166982, 0.0015082783065736294, 0.001621243660338223, 0.001323142321780324, 0.001251866458915174, 0.0012847160687670112, 0.0009752091718837619]
acc = [0.8717620372772217, 0.9831374287605286, 0.9891902804374695, 0.9920413494110107, 0.9937642216682434, 0.9951973557472229, 0.995700478553772, 0.9966305494308472, 0.997072696685791, 0.9977892637252808, 0.9979112148284912, 0.9982619285583496, 0.9983686208724976, 0.9988412857055664, 0.9990394711494446, 0.9990547299385071, 0.9991766810417175, 0.999359667301178, 0.9994053840637207, 0.9994053840637207, 0.9994663596153259, 0.9995578527450562, 0.9995578527450562, 0.9997408390045166, 0.9996950626373291, 0.9996646046638489, 0.9997712969779968, 0.9997255802154541, 0.9998018145561218, 0.999862790107727]
val_loss = [0.11911491304636002, 0.13999217748641968, 0.10977234691381454, 0.10404161363840103, 0.09234873950481415, 0.12978146970272064, 0.11937367916107178, 0.1358346790075302, 0.10977641493082047, 0.14471347630023956, 0.11928091198205948, 0.11932700127363205, 0.111799456179142, 0.11673298478126526, 0.11826559156179428, 0.11849474161863327, 0.15743288397789001, 0.12659917771816254, 0.11449845880270004, 0.12954489886760712, 0.13206923007965088, 0.11954184621572495, 0.12777453660964966, 0.14072054624557495, 0.12899461388587952, 0.1381428986787796, 0.13359296321868896, 0.14775650203227997, 0.1680537909269333, 0.12599290907382965]
val_acc = [0.961809515953064, 0.9565062522888184, 0.9674330949783325, 0.9691415429115295, 0.9720956683158875, 0.9654399156570435, 0.9697821736335754, 0.9660806059837341, 0.9729142785072327, 0.9674330949783325, 0.970173716545105, 0.973376989364624, 0.9732702374458313, 0.9719533324241638, 0.9734837412834167, 0.9729498624801636, 0.967041552066803, 0.9725227952003479, 0.975121021270752, 0.9718821048736572, 0.9735905528068542, 0.9747650623321533, 0.9723803997039795, 0.9722736477851868, 0.9740176796913147, 0.9708855152130127, 0.973376989364624, 0.9724159836769104, 0.9683584570884705, 0.9748718738555908]

plt.plot(loss, label='loss')
plt.plot(acc, label = 'acc')
plt.plot(val_loss, label = 'val_loss')
plt.plot(val_acc, label = 'val_acc')

plt.legend()
plt.show()