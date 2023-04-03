import os

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def tile_video_linear(file_name):

    '''Tiles video clips in sequence. Place in folder.  Provide destination file name and run.
    example:

    tile_video_linear("guts.mp4")
    '''
    all_files = os.listdir()
    all_clips = []

    for i in all_files:
        if i.endswith(".mp4"):
            clip = VideoFileClip(i)
            all_clips.append(clip)

    final_clip = concatenate_videoclips(all_clips)

    final_clip.write_videofile(file_name)



def video_speed(video, speed_factor, new_file_name):
    """Place in folder. Provide start file, steep and destination file name:
    example:

    video_speed("guts.mp4", 4, "fast_guts.mp4")

    """
    clip = VideoFileClip(video)
    final_clip = clip.fx(vfx.speedx, speed_factor)
    final_clip.write_videofile(new_file_name)

