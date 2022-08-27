from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': '<</PATH/TO/>>secure-connect-testing-1.zip'
}
auth_provider = PlainTextAuthProvider('LBowjsOjnzbmhabzUTvvojxN', 'GQADoHtukd5ULJUM_pSvRqg_ZB8xtri11lZfx6_HFvDWzWYYlpK5Xq.lw5BIIrwqZ-SmcLZtEzC,jYyiGdJXjdCGM2-JZX0B,OOPQps460zcPm-5T_M_Ceubvmau0BfT')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
'''
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': '/path/to/secure-connect-testing1.zip'
}
auth_provider = PlainTextAuthProvider('LBowjsOjnzbmhabzUTvvojxN', 'GQADoHtukd5ULJUM_pSvRqg_ZB8xtri11lZfx6_HFvDWzWYYlpK5Xq.lw5BIIrwqZ-SmcLZtEzC,jYyiGdJXjdCGM2-JZX0B,OOPQps460zcPm-5T_M_Ceubvmau0BfT')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
'''
