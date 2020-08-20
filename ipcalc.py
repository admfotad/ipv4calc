

def spr(ipadr,ipsubnet):
    ip_pack=[]
    adres=ipadr
    maska=ipsubnet

    def wczytaj(adres,maska):
        blad=False
        try:
            adres_x = [int(s) for s in adres.split('.')]
            maska_y = [int(s) for s in maska.split('.')]
        except:
            blad=True
        if len(adres_x)>4 or len(maska_y)>4:
            blad=True
        for n in range(len(adres_x)):
            if adres_x[n]>255 or adres_x[n]<0:
                blad=True
#        print(adres_x[n])
        if blad:
            return 'Error'
        else:
            return adres_x,maska_y

    try:
        x,y =wczytaj(adres,maska)
    except:
        print('Error reading data')
        exit()


    if 'Error' in x:
        print('Error reading data')
        exit()

#y = [int(s) for s in mask.split('.')]
    temp_adr=str(x[0])+'.'+str(x[1])+'.'+str(x[2])+'.'+str(x[3])
    temp_net=str(y[0])+'.'+str(y[1])+'.'+str(y[2])+'.'+str(y[3])
    ip_pack.append(temp_adr)
    ip_pack.append(temp_net)
#    print(x[0],x[1],x[2],x[3])
#    print(y[0],y[1],y[2],y[3])

    def mask31():
        adres1=str(x[0])+'.'+str(x[1])+'.'+str(x[2])+'.'+str(x[3])
        adres2=str(x[0])+'.'+str(x[1])+'.'+str(x[2])+'.'+str(x[3]+1)
        maska=str(y[0])+'.'+str(y[1])+'.'+str(y[2])+'.'+str(y[3])
        return adres1,adres2,maska

    def mask2bit(q):
        bit=0
        for p in q:
            if p==255:
                bit=bit+8
            elif p==254:
                bit=bit+7
            elif p==252:
                bit=bit+6
            elif p==248:
                bit=bit+5
            elif p==240:
                bit=bit+4
            elif p==224:
                bit=bit+3
            elif p==192:
                bit=bit+2
            elif p==128:
                bit=bit+1
        return bit

    ip_pack.append(mask2bit(y))

    if mask2bit(y)<31:
#binary=bin(x1&y1)
        as1=x[0]&y[0]
        as2=x[1]&y[1]
        as3=x[2]&y[2]
        as4=x[3]&y[3]
#        print('Adres sieci:',as1,as2,as3,as4)  #print(y[2],format(y[2],'08b'))
        temp_siec=str(as1)+'.'+str(as2)+'.'+str(as3)+'.'+str(as4)
        ip_pack.append(temp_siec)
        licz=-1
        for a in y:
            licz=licz+1
            if y[licz]<255:
                break
        def maska2inv_cidr(j):  #maska do cidr dziesietnie
            try:
                c1=255-j[0]
                c2=255-j[1]
                c3=255-j[2]
                c4=255-j[3]
            except:
                return 'Error'
            return c1,c2,c3,c4

        def max_hosts(netmask_length):
            temp=2**(32-netmask_length)-2
            return temp

        def max_subnets(netmask_length):
            temp=2**(32-netmask_length)
            return temp

        ip_pack.append(max_hosts(mask2bit(y)))
        ip_pack.append(max_subnets(mask2bit(y)))
#        print('Maksymalna ilosc hostow:',max_hosts(mask2bit(y)))
#        print('Ilosc podsieci: ',max_subnets(mask2bit(y)))

        def broadcast():
            u,j,m,i=maska2inv_cidr(y)
#            print('Inverted binary CIDR ',u,j,m,i)  # inverted binary CIDR
#    i=0
#    for n in range(0,4):
            b0=as1|u
            b1=as2|j
            b2=as3|m
            b3=as4|i
#    print('#',as4,i)
#        i=i+1
            return b0,b1,b2,b3

        ba1,ba2,ba3,ba4=broadcast()
        temp_broadcast=str(ba1)+'.'+str(ba2)+'.'+str(ba3)+'.'+str(ba4)
        ip_pack.append(temp_broadcast)
        temp_host_min=str(as1)+'.'+str(as2)+'.'+str(as3)+'.'+str(as4+1)
        ip_pack.append(temp_host_min)
        temp_host_max=str(ba1)+'.'+str(ba2)+'.'+str(ba3)+'.'+str(ba4-1)
        ip_pack.append(temp_host_max)
#        print('broadcast: ',ba1,ba2,ba3,ba4)
#        print('host min: ',as1,as2,as3,as4+1)
#        print('host max: ',ba1,ba2,ba3,ba4-1)

        return ip_pack

    else:
        dz1,dz2,dzm=mask31()
        ip_pack.append(dz1)
        ip_pack.append(dz2)
        ip_pack.append(dzm)
        return ip_pack
#        print(dz1,dz2,dzm)