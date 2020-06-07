"""
Library for SBS
"""
import libvirt
import uuid


series = [ 'a', 'ap', 'd', 'e', 'f', 'k', 'kde', 'kdei', 'l', 'n', 
           't', 'tcl', 'x', 'xap', 'xfce', 'y' ]



def lock():
    '''
    Crear un archivo de bloqueo para evitar que la herramienta corra dos veces
    '''
    pass

def unlock():
    '''
    Elimina el archivo de bloqueo al completa ejecución
    '''
    pass

def queue():
    '''
    Recibe dos parámetros la categoría de paquetes, y el nombre del paquete.
    Agrega ambos parámetros a la cola de builds
    '''
    pass


def queueall():
    '''
    Busca todos los archivos de tipo SlackBuild y los agrega todos a la cola
    de compilado. Para ejecuta antes de un release, luego de cambio de
    compilador, de opciones de compilador, para verificación de seguridad, etc
    '''

def build():
    '''
    Cuando hay paquetes pendientes por compilar, toma el primero y lo compila,
    guardando bitácoras y el paquete resultante
    - Copia la máquina virtual de Slackware-build, que contiene una
      una instalación completa de Slackware.
    - Monta el repositorio por medio de sshfs.
    - Ejecuta build del paquete.
    - Fecha de inicio y finalización

    Se repite hasta que no existan paquetes en la cola.
    '''
    try:
        conn = libvirt.open('qemu+ssh://fede2@172.20.1.6/system')
    except libvirt.libvirtError:
        print('Failed to open connection to the hypervisor')
        sys.exit(1)
    stgvol_xml = """
<volume>
  <name>sbs-template.qcow2</name>
  <allocation>0</allocation>
  <capacity unit="G">61</capacity>
  <target>
    <path>/var/lib/virt/images/sbs.qcow2</path>
    <permissions>
      <owner>0</owner>
      <group>0</group>
      <mode>0744</mode>
      <label>virt_image_t</label>
    </permissions>
  </target>
</volume>"""
    stgvol_xml2 = """
<volume>
  <name>sbs-build.qcow2</name>
  <allocation>0</allocation>
  <capacity unit="G">61</capacity>
  <target>
    <path>/var/lib/virt/images/sbs-build.qcow2</path>
    <permissions>
      <owner>0</owner>
      <group>0</group>
      <mode>0744</mode>
      <label>virt_image_t</label>
    </permissions>
  </target>
</volume>"""
    poolName = 'default'
    pool = conn.storagePoolLookupByName(poolName)
    if pool == None:
        print('Failed to locate any StoragePool objects.', file=sys.stderr)
        exit(1)
    sp = conn.storagePoolLookupByName(poolName)
    if sp == None:
        print('Failed to find storage pool '+pool, file=sys.stderr)
        exit(1)
    
    stgvols = sp.listVolumes()
    print('Storage pool: '+poolName)
    for stgvol in stgvols :
        print('  Storage vol: '+stgvol)

    # create a new storage volume
    stgvol = pool.createXML(stgvol_xml, 0)
    print(type(stgvol))
    print(dir(stgvol))
    if stgvol == None:
        print('Failed to create a  StorageVol object.', file=sys.stderr)
        exit(1)
    
    # now clone the existing storage volume
    print('This could take some time...')
    stgvol2 = pool.createXMLFrom(stgvol_xml2, stgvol, 0)
    if stgvol2 == None:
        print('Failed to clone a  StorageVol object.', file=sys.stderr)
        exit(1)
    print("borrando")
    input()
    # remove the cloned storage volume
    # physically remove the storage volume from the underlying disk media
    stgvol2.wipe(0)
    # logically remove the storage volume from the storage pool
    stgvol2.delete(0)
    
    # remove the storage volume
    # physically remove the storage volume from the underlying disk media
    #stgvol.wipe(0)
    # logically remove the storage volume from the storage pool
    stgvol.delete(0)

    conn.close()

def qa():
    '''
    A los paquetes completados, les ejecuta un control de calidad:
    - Conteo de archivos de este paquete versus el amd64
    - Strips de archivos
    - Presencia de ligas
    - Archivos binarios con librerías no encontradas
    '''
    pass

def to_incomming():
    '''
    Copia el archivo de paquete completo, y sus bitácoras con estadísticas
    hacia un espacio dedicado en el directorio de sshfs
    '''

def vmrebuild():
    '''
    Reconstruye la máquina virtual. Recomendado luego de cambios de
    compilador, glibc, kernel, librerías importantes
    - Reconstruye chroot
    - Instala kernel
    - Corre virt-make-fs para traducir de chroot a .img para qemu
    - Copia llaves de ssh para montado de repo, y salida de paquetes
    '''
    pass
