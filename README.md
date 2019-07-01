# python1
Python based projects - early ones

dnsparse: tool used to parse and reformat named zone files into .yml files.
--------
...
 EXAMPLE output: 
          - name:  mon
            ip:  11.55.1.22
          - name:  go
            ip:  11.55.1.27
          - name:  f10sw
            ip:  11.55.1.29
          - name:  esxi01
            ip:  11.55.1.41
          - name:  esxi02
            ip:  11.55.1.42 
...

 This can now be read directly into your bind playbook or just cut/paste.
