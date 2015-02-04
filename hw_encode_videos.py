import heywatch
import time
# import simplejson as json


def get_format_id(format_name):
    if format_name == 'android_LQ':
        return '42780'
    elif format_name == 'android_MQ':
        return '42781'
    elif format_name == 'android_HQ':
        return '42781'

username = 'HW-API-Key'
# heywatch api key
password = 'XXXXXX'

hw = heywatch.API(username,
                  password,
                  disable_ssl_certificate_validation=True)

# downloads = hw.all("download")
# print json.dumps(downloads, indent=4, separators=(',', ': '))

# ping_url = ''
# format_id = get_format_id('android_MQ')
format_id = 'mp4_360p'
# output_url = 'az://ksvideos:JV9oDDPcRGxfW+uQ5E6Zl/Fi9mvE0WbUTIHMd4M55W5Yv+WrO4F6q99xD1sLN+DESHGtRse8HhVYV7+yjOmHzw==@test'
output_url = 'az://ksvideos:JV9oDDPcRGxfW+uQ5E6Zl/Fi9mvE0WbUTIHMd4M55W5Yv+WrO4F6q99xD1sLN+DESHGtRse8HhVYV7+yjOmHzw==@videos'
# output_url = 'az://portalvhds3cj1mjnqkvnwn:7QMHy5btCYCgD5aKCEiNH9H7EYu3444yM061tiL7Y6V3pAWEZlLhUj+B7tSUF2hvI4si/Q1yBF2/pPHeRZRIiw==@test'
# output_url = 's3://AKIAIYWCHLTIH6J3TQXA:Ok0oprgEpYs+SBaMF+MDayBcAKuDyI9YxtL4QhhY@ksvideosrepo'

for x in range(377, 388):

    print 'Begin with video ' + str(x)
    video_title = str(x)

    url = 'https://s3-us-west-2.amazonaws.com/videos-v1/' + video_title + '.mp4'
    # url = 'https://s3.amazonaws.com/videos-v2/' + video_title + '.avi'

    video_download = hw.create('download',
                               url=url,
                               title=video_title)
    print 'Begin download'

    while True:
        time.sleep(5)
        download_obj = hw.info('download', video_download['id'])
        if download_obj['status'] == 'finished':
            print 'Finish download'
            break
        elif download_obj['status'] == 'error':
            print 'Error download'
            break

    video_id = download_obj['video_id']
    if video_id:
        job_created = hw.create('job',
                                video_id=video_id,
                                format_id=format_id,
                                keep_video_size=False,
                                output_url=output_url)
        print 'Begin Job'

        # while True:
        #     time.sleep(5)
        #     job_obj = hw.info('job', job_created['id'])
        #     if job_obj['status'] == 'finished':
        #         print 'Finish Job'
        #         break
        #     elif job_obj['status'] == 'error':
        #         print 'Error Job'
        #         break


# Para verificar que las canciones si fueron transferidas correctamente
# a Azure, se debe correr la siguiente linea en shell

# for i in {1..513} do curl -I ksvideos.blob.core.windows.net/videos/$i.mp4 | grep 'HTTP/1.1 404' echo $i done
