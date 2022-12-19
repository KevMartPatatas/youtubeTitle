from moviepy.editor import *

# clip1 = mpy.ColorClip((1280, 720), col=(255,0,0))
# clip1 = clip1.set_duration(5)

# clip2 = mpy.ImageClip("curifeos.jpg")
# clip2 = clip2.set_duration(10)

# final_video = mpy.concatenate_videoclips([clip1, clip2], method="compose")
# final_video.write_videofile("composition.mp4", fps=24)

gif = VideoFileClip('gif_barra_roja.gif')
print(gif.duration)
# videClip = videClip.set_duration(10)
# print(videClip.duration)
# final = CompositeVideoClip([videClip])
# final.write_videofile("Prueba.mp4", fps=10)

# print(videClip.fps)
# print(duracion)
# print(duracion * videClip.fps)
# # videClip = videClip.fx(vfx.resize)
# videClip = videClip.resize(width=50)
# ancho, alto = videClip.size
# print(ancho, alto)
# clipMarco = ImageClip("curifeos.jpg")
# clipMarco = clipMarco.set_duration(duracion)

# videoFinal = CompositeVideoClip([clipMarco, videClip.set_position((40, 150))])
# videoFinal.write_videofile("Prueba.mp4", fps=10)

