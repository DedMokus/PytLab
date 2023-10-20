import wget
import concurrent.futures

urls = ["https://w.forfun.com/fetch/02/0261dfae0e4904627653a2d6d5de1a4e.jpeg",
        "https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotov-20.jpg",
        "https://i.artfile.ru/1920x1200_454642_[www.ArtFile.ru].jpg" ,
        "https://w-dog.ru/wallpapers/5/18/289291145046987/evropejskaya-koshka-dikij-kot-morda-vzglyad.jpg",
        "https://i.pinimg.com/736x/c9/61/7a/c9617a252d30299a52122e8f42c3a40e.jpg",
        "https://pic.rutubelist.ru/video/4d/aa/4daaa809bc617265266d5247860bbe9b.jpg",
        "https://avatars.mds.yandex.net/get-mpic/5205776/img_id7887798007625704971.jpeg/orig",
        "https://wp-s.ru/wallpapers/3/18/486297853777193/seryj-vislouxij-kot-s-zh-ltymi-glazami.jpg",
        "https://images.wallpaperscraft.ru/image/single/kot_udivlenie_vzgliad_96597_1280x1024.jpg",
        "https://www.funnyart.club/uploads/posts/2022-12/1671990494_www-funnyart-club-p-memi-s-kotom-vkontakte-34.jpg"]



def SaveFileURL(url,i):
    wget.download(url,f"cat{i}.jpg")

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(SaveFileURL, url,i) for url,i in zip(urls, range(len(urls)))]
    for future in concurrent.futures.as_completed(futures):
        pass