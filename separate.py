import os
import shutil

a = ['f1_script2_cleanraw', 'f8_script3_cleanraw', 'f8_script5_cleanraw', 'm8_script2_cleanraw', 'm8_script3_cleanraw',
     'm8_script4_cleanraw', 'f7_script4_ipadflat_confroom1', 'm3_script3_ipadflat_confroom1',
     'm6_script1_ipadflat_confroom1', 'm6_script4_ipadflat_confroom1', 'f1_script2_ipadflat_office1',
     'f7_script3_ipadflat_office1', 'f7_script4_ipadflat_office1', 'f8_script3_ipadflat_office1',
     'm3_script3_ipadflat_office1', 'm3_script4_ipadflat_office1', 'f8_script3_ipad_balcony1',
     'm3_script1_ipad_balcony1', 'f8_script4_ipad_bedroom1', 'm3_script2_ipad_bedroom1', 'm6_script3_ipad_bedroom1',
     'm6_script5_ipad_bedroom1', 'm8_script3_ipad_bedroom1', 'f7_script2_ipad_confroom1', 'f8_script4_ipad_confroom1',
     'm3_script4_ipad_confroom1', 'm6_script2_ipad_confroom1', 'm8_script2_ipad_confroom1', 'm8_script3_ipad_confroom1',
     'f1_script3_ipad_confroom2', 'f7_script1_ipad_confroom2', 'f7_script2_ipad_confroom2', 'm3_script5_ipad_confroom2',
     'm6_script2_ipad_confroom2', 'm6_script3_ipad_confroom2', 'm8_script1_ipad_confroom2',
     'f7_script1_ipad_livingroom1', 'f7_script4_ipad_livingroom1', 'f8_script5_ipad_livingroom1',
     'm3_script2_ipad_livingroom1', 'm6_script4_ipad_livingroom1', 'm6_script5_ipad_livingroom1',
     'm8_script5_ipad_livingroom1', 'f1_script3_ipad_office1', 'f7_script1_ipad_office1', 'm8_script5_ipad_office1',
     'f1_script4_ipad_office2', 'f7_script2_ipad_office2', 'm3_script2_ipad_office2', 'f1_script3_iphone_balcony1',
     'f7_script5_iphone_balcony1', 'f8_script2_iphone_balcony1', 'f8_script3_iphone_balcony1',
     'm3_script3_iphone_balcony1', 'm6_script3_iphone_balcony1', 'm6_script5_iphone_balcony1',
     'f1_script2_iphone_bedroom1', 'f8_script3_iphone_bedroom1', 'f8_script4_iphone_bedroom1',
     'm8_script5_iphone_bedroom1']
b = ['f10_script2_cleanraw', 'f2_script3_cleanraw', 'f4_script4_cleanraw', 'f5_script1_cleanraw', 'f6_script5_cleanraw',
     'f9_script2_cleanraw', 'm2_script5_cleanraw', 'm5_script2_cleanraw', 'f10_script5_ipadflat_confroom1',
     'f4_script3_ipadflat_confroom1', 'f9_script3_ipadflat_confroom1', 'm1_script5_ipadflat_confroom1',
     'm2_script4_ipadflat_confroom1', 'm4_script2_ipadflat_confroom1', 'm7_script4_ipadflat_confroom1',
     'm9_script5_ipadflat_confroom1', 'f10_script4_ipadflat_office1', 'f2_script2_ipadflat_office1',
     'f4_script1_ipadflat_office1', 'f5_script1_ipadflat_office1', 'f5_script5_ipadflat_office1',
     'f6_script1_ipadflat_office1', 'm10_script1_ipadflat_office1', 'm2_script3_ipadflat_office1',
     'm4_script3_ipadflat_office1', 'm7_script2_ipadflat_office1', 'm7_script3_ipadflat_office1',
     'm9_script3_ipadflat_office1', 'f10_script3_ipad_balcony1', 'f2_script3_ipad_balcony1', 'f4_script5_ipad_balcony1',
     'f5_script1_ipad_balcony1', 'f5_script3_ipad_balcony1', 'f5_script4_ipad_balcony1', 'f6_script4_ipad_balcony1',
     'f9_script1_ipad_balcony1', 'f9_script3_ipad_balcony1', 'm10_script3_ipad_balcony1', 'm10_script4_ipad_balcony1',
     'm1_script5_ipad_balcony1', 'm9_script4_ipad_balcony1', 'f2_script1_ipad_bedroom1', 'f4_script4_ipad_bedroom1',
     'f6_script1_ipad_bedroom1', 'f9_script3_ipad_bedroom1', 'm4_script2_ipad_bedroom1', 'm7_script2_ipad_bedroom1',
     'm7_script5_ipad_bedroom1', 'f10_script3_ipad_confroom1', 'f3_script4_ipad_confroom1', 'f5_script5_ipad_confroom1',
     'f6_script5_ipad_confroom1', 'm4_script3_ipad_confroom1', 'm9_script4_ipad_confroom1', 'm9_script5_ipad_confroom1',
     'f2_script2_ipad_confroom2', 'f4_script3_ipad_confroom2', 'm1_script2_ipad_confroom2', 'm1_script5_ipad_confroom2',
     'm5_script5_ipad_confroom2', 'f2_script4_ipad_livingroom1', 'f3_script4_ipad_livingroom1',
     'f4_script2_ipad_livingroom1', 'f5_script3_ipad_livingroom1', 'f6_script1_ipad_livingroom1',
     'f6_script4_ipad_livingroom1', 'm10_script5_ipad_livingroom1', 'm2_script2_ipad_livingroom1',
     'm2_script5_ipad_livingroom1', 'm4_script4_ipad_livingroom1', 'm4_script5_ipad_livingroom1',
     'm5_script1_ipad_livingroom1', 'm9_script2_ipad_livingroom1', 'f10_script1_ipad_office1',
     'f10_script2_ipad_office1', 'f10_script3_ipad_office1', 'f10_script5_ipad_office1', 'f2_script3_ipad_office1',
     'f5_script1_ipad_office1', 'f6_script5_ipad_office1', 'f9_script1_ipad_office1', 'm10_script1_ipad_office1',
     'm10_script4_ipad_office1', 'm1_script2_ipad_office1', 'm2_script1_ipad_office1', 'm2_script3_ipad_office1',
     'm2_script4_ipad_office1', 'm2_script5_ipad_office1', 'm5_script2_ipad_office1', 'm7_script2_ipad_office1',
     'm7_script5_ipad_office1', 'f2_script3_ipad_office2', 'f4_script1_ipad_office2', 'f5_script1_ipad_office2',
     'm1_script2_ipad_office2', 'm2_script4_ipad_office2', 'm4_script1_ipad_office2', 'm4_script2_ipad_office2',
     'm4_script4_ipad_office2', 'm4_script5_ipad_office2', 'm5_script2_ipad_office2', 'm5_script3_ipad_office2',
     'm5_script5_ipad_office2', 'm7_script2_ipad_office2', 'f10_script1_iphone_balcony1', 'f10_script4_iphone_balcony1',
     'f2_script3_iphone_balcony1', 'f2_script4_iphone_balcony1', 'f2_script5_iphone_balcony1',
     'm1_script2_iphone_balcony1', 'm2_script2_iphone_balcony1', 'm2_script4_iphone_balcony1',
     'm4_script4_iphone_balcony1', 'm4_script5_iphone_balcony1', 'm7_script3_iphone_balcony1',
     'm7_script4_iphone_balcony1', 'm9_script2_iphone_balcony1', 'm9_script4_iphone_balcony1',
     'f2_script5_iphone_bedroom1', 'f4_script3_iphone_bedroom1', 'f5_script2_iphone_bedroom1',
     'f5_script4_iphone_bedroom1', 'f6_script2_iphone_bedroom1', 'f6_script3_iphone_bedroom1',
     'm10_script3_iphone_bedroom1', 'm10_script4_iphone_bedroom1', 'm1_script2_iphone_bedroom1',
     'm4_script3_iphone_bedroom1', 'm4_script5_iphone_bedroom1', 'm9_script3_iphone_bedroom1',
     'f3_script4_iphone_livingroom1', 'f3_script5_iphone_livingroom1', 'f4_script2_iphone_livingroom1',
     'f4_script5_iphone_livingroom1', 'f6_script1_iphone_livingroom1', 'f9_script2_iphone_livingroom1',
     'm1_script2_iphone_livingroom1', 'm2_script4_iphone_livingroom1', 'm4_script4_iphone_livingroom1',
     'm7_script1_iphone_livingroom1']

dirpath = 'daps_Data\\Spectrograms_mel_16_normalized_cropped_training\\Images'
distpath = 'daps_Data\\Spectrograms_mel_16_normalized_cropped_test\\Images'
for filename in os.listdir(dirpath):
    if any(filename.startswith(name) for name in a) or any(filename.startswith(name) for name in b):
        full_path = os.path.join(dirpath, filename)
        shutil.move(full_path, distpath)


