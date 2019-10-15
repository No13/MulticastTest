In Cisco ACI werkt multicast net een beetje anders dan anders.


Als je geen multicast-routing aan hebt staan wordt het op l2 binnen 1 bridge domain wel geforward. Dit wordt dan als semi-broadcast verkeer behandeld.


Zodra je multicast-routing inschakelt wordt het verkeer echter gerouteerd en gaat ineens de TTL een rol spelen:
https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/white-paper-c11-739609.html

> Multicast routing with Cisco ACI is supported with an “always route” approach whereby TTL decrement is applied to the traffic even if the source and the receivers are part of the same IP subnet. It is worth noticing how intrasubnet multicast forwarding could also be achieved with Cisco ACI without enabling multicast routing and just handling those flows as Layer 2 multicast communication. However, those two behaviors are mutually exclusive and once multicast routing is enabled for a bridge domain, the “always route” approach will be the one in use.

De scripts in deze map maken het mogelijk om te loggen of verkeer wordt verzonden vanuit de AACC (234.5.6.27 port 6070) (tel.py)

Ook is het mogelijk om met send-msg.py en receive-msg.py verkeer te sturen en ontvangen naar 234.5.6.2 poort 6666

Pas op: receive-msg.py en tel.py dienen met python 3.7 te worden gestart. Mogelijk dat send-msg.py alleen met python2 werkt.