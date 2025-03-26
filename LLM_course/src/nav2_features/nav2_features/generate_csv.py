
import csv
import random
from geometry_msgs.msg import PoseStamped
import tf_transformations

###################
# first room center waypoint
waypoint1 = PoseStamped()
waypoint1.header.frame_id = 'map'
waypoint1.pose.position.x = -1.2125468254089355
waypoint1.pose.position.y = -1.2125468254089355
waypoint1.pose.orientation.z = -0.4289825503471511
waypoint1.pose.orientation.w = 0.903312776117804

# first room corridor waypoint
waypoint2 = PoseStamped()
waypoint2.header.frame_id = 'map'
waypoint2.pose.position.x = 0.14680004119873047
waypoint2.pose.position.y = -1.638221263885498
waypoint2.pose.orientation.z = 0.24422903497273388
waypoint2.pose.orientation.w = 0.9697175766563619

# kitchen sink waypoint
waypoint3 = PoseStamped()
waypoint3.header.frame_id = 'map'
waypoint3.pose.position.x = 3.1755123138427734
waypoint3.pose.position.y = -1.3481559753417969
waypoint3.pose.orientation.z = 0.013796661432267049
waypoint3.pose.orientation.w = 0.9999048215371918

# kitchen window waypoint
waypoint4 = PoseStamped()
waypoint4.header.frame_id = 'map'
waypoint4.pose.position.x = 2.1198079586029053
waypoint4.pose.position.y = 3.1093714237213135
waypoint4.pose.orientation.z = 0.6879698862097293
waypoint4.pose.orientation.w = 0.725739233932252

###################
# bedroom waypoint
waypoint5 = PoseStamped()
waypoint5.header.frame_id = 'map'
waypoint5.pose.position.x = -2.7975411415100098
waypoint5.pose.position.y = 4.356760501861572
waypoint5.pose.orientation.z = 0.6997299401403602
waypoint5.pose.orientation.w = 0.7144074543782196

# bedroom bed
waypoint6 = PoseStamped()
waypoint6.header.frame_id = 'map'
waypoint6.pose.position.x = -1.0502538681030273
waypoint6.pose.position.y = 8.056700706481934
waypoint6.pose.orientation.z = -0.9999191920932438
waypoint6.pose.orientation.w = 0.012712564005518146

# bedroom carpet
waypoint7 = PoseStamped()
waypoint7.header.frame_id = 'map'
waypoint7.pose.position.x = -2.6430296897888184
waypoint7.pose.position.y = 5.9215288162231445
waypoint7.pose.orientation.z = 0.6916271676170973
waypoint7.pose.orientation.w = 0.7222547064671518

# bedroom dresser
waypoint8 = PoseStamped()
waypoint8.header.frame_id = 'map'
waypoint8.pose.position.x = -4.29341983795166
waypoint8.pose.position.y = 7.299586296081543
waypoint8.pose.orientation.z = -0.9991987291974286
waypoint8.pose.orientation.w = 0.04002373758463568

# bedroom plant
waypoint9 = PoseStamped()
waypoint9.header.frame_id = 'map'
waypoint9.pose.position.x = -4.663019180297852
waypoint9.pose.position.y = 9.353409767150879
waypoint9.pose.orientation.z = 0.8151024835963414
waypoint9.pose.orientation.w = 0.5793167883248991

# bedroom painting
waypoint10 = PoseStamped()
waypoint10.header.frame_id = 'map'
waypoint10.pose.position.x = -4.29341983795166
waypoint10.pose.position.y = 7.299586296081543
waypoint10.pose.orientation.z = -0.9991987291974286
waypoint10.pose.orientation.w = 0.04002373758463568


##########################
# office
waypoint11 = PoseStamped()
waypoint11.header.frame_id = 'map'
waypoint11.pose.position.x = -6.131107330322266
waypoint11.pose.position.y = 1.9277256727218628
waypoint11.pose.orientation.z = 0.9999717404803861
waypoint11.pose.orientation.w = 0.0075178614397557195

# office table
waypoint12 = PoseStamped()
waypoint12.header.frame_id = 'map'
waypoint12.pose.position.x = -7.678760051727295
waypoint12.pose.position.y = 1.9843963384628296
waypoint12.pose.orientation.z = -0.9999760574199975
waypoint12.pose.orientation.w = 0.006919868984150821

# office chair
waypoint13 = PoseStamped()
waypoint13.header.frame_id = 'map'
waypoint13.pose.position.x = -9.9851655960083
waypoint13.pose.position.y = 1.871001958847046
waypoint13.pose.orientation.z = 0.005006256786583879
waypoint13.pose.orientation.w = 0.9999874686179756

# office plant
waypoint14 = PoseStamped()
waypoint14.header.frame_id = 'map'
waypoint14.pose.position.x = -9.97191047668457
waypoint14.pose.position.y = 0.6397298574447632
waypoint14.pose.orientation.z = -0.8794235415391699
waypoint14.pose.orientation.w = 0.476040160686789

# office window
waypoint15 = PoseStamped()
waypoint15.header.frame_id = 'map'
waypoint15.pose.position.x = -10.25112533569336
waypoint15.pose.position.y = 1.8134584426879883
waypoint15.pose.orientation.z = -0.9999875011773998
waypoint15.pose.orientation.w = 0.004999748891665366

# office painting
waypoint16 = PoseStamped()
waypoint16.header.frame_id = 'map'
waypoint16.pose.position.x = -8.255940437316895
waypoint16.pose.position.y = 3.4991869926452637
waypoint16.pose.orientation.z = 0.6929374411590997
waypoint16.pose.orientation.w = 0.72099771333887

####################
# living room
waypoint17 = PoseStamped()
waypoint17.header.frame_id = 'map'
waypoint17.pose.position.x = -5.5337934494018555
waypoint17.pose.position.y = -2.4765660762786865
waypoint17.pose.orientation.z = 0.9999960690691245
waypoint17.pose.orientation.w = 0.002803898410964191

# living room sofa/couch
waypoint18 = PoseStamped()
waypoint18.header.frame_id = 'map'
waypoint18.pose.position.x = -5.861964702606201
waypoint18.pose.position.y = -4.7797651290893555
waypoint18.pose.orientation.z = 0.7179730381796221
waypoint18.pose.orientation.w = 0.6960709133752989

# living room table
waypoint19 = PoseStamped()
waypoint19.header.frame_id = 'map'
waypoint19.pose.position.x = -7.116544246673584
waypoint19.pose.position.y = -2.774833917617798
waypoint19.pose.orientation.z = 0.9997203472743579
waypoint19.pose.orientation.w = 0.023647986079947007

# living room tv/television
waypoint20 = PoseStamped()
waypoint20.header.frame_id = 'map'
waypoint20.pose.position.x = -7.367372512817383
waypoint20.pose.position.y = -1.2271184921264648
waypoint20.pose.orientation.z = 0.6919450914490862
waypoint20.pose.orientation.w = 0.72195013014717

# living room lamp
waypoint21 = PoseStamped()
waypoint21.header.frame_id = 'map'
waypoint21.pose.position.x = -9.099431037902832
waypoint21.pose.position.y = -0.9577126502990723
waypoint21.pose.orientation.z = 0.9992627931306665
waypoint21.pose.orientation.w = 0.0383910180211296

########################
# bathroom/restroom/toilet/washroom
waypoint22 = PoseStamped()
waypoint22.header.frame_id = 'map'
waypoint22.pose.position.x = -3.243408203125
waypoint22.pose.position.y = -5.089259147644043
waypoint22.pose.orientation.z = -0.6887441683779368
waypoint22.pose.orientation.w = 0.7250044624175662

# bathroom/restroom/toilet/washroom sink or mirror
waypoint23 = PoseStamped()
waypoint23.header.frame_id = 'map'
waypoint23.pose.position.x = -3.462225914001465
waypoint23.pose.position.y = -7.1564249992370605
waypoint23.pose.orientation.z = -0.44550069187624797
waypoint23.pose.orientation.w = 0.8952815945487679

# bathroom/restroom/toilet/washroom toilet 
waypoint24 = PoseStamped()
waypoint24.header.frame_id = 'map'
waypoint24.pose.position.x = -3.74117374420166
waypoint24.pose.position.y = -7.161655902862549
waypoint24.pose.orientation.z = -0.9990216084089449
waypoint24.pose.orientation.w = 0.044224720824497965

# bathroom/restroom/toilet/washroom shower 
waypoint25 = PoseStamped()
waypoint25.header.frame_id = 'map'
waypoint25.pose.position.x = -3.145960807800293
waypoint25.pose.position.y = -6.036275386810303
waypoint25.pose.orientation.z = -0.9990977182131023
waypoint25.pose.orientation.w = 0.04247057170997715

##########################
# hall/ entrance hall/ foyer / lobby
waypoint26 = PoseStamped()
waypoint26.header.frame_id = 'map'
waypoint26.pose.position.x = 1.2582759857177734
waypoint26.pose.position.y = -6.1945648193359375
waypoint26.pose.orientation.z = -0.6847081843315889
waypoint26.pose.orientation.w = 0.7288173312355702

# hall/ entrance hall/ foyer / lobby sofa/couch 1
waypoint27 = PoseStamped()
waypoint27.header.frame_id = 'map'
waypoint27.pose.position.x = -0.5546073913574219
waypoint27.pose.position.y = -9.387605667114258
waypoint27.pose.orientation.z = 0.02169910396680736
waypoint27.pose.orientation.w = 0.9997645467243963

# hall/ entrance hall/ foyer / lobby sofa/couch 2
waypoint28 = PoseStamped()
waypoint28.header.frame_id = 'map'
waypoint28.pose.position.x = 3.959217071533203
waypoint28.pose.position.y = -13.624397277832031
waypoint28.pose.orientation.z = 0.6998396140845212
waypoint28.pose.orientation.w = 0.7143000171902758

# hall/ entrance hall/ foyer / lobby sofa/couch
# same as sofa 1

# hall/ entrance hall/ foyer / lobby window
waypoint29 = PoseStamped()
waypoint29.header.frame_id = 'map'
waypoint29.pose.position.x = 3.7871317863464355
waypoint29.pose.position.y = -7.569762706756592
waypoint29.pose.orientation.z = -0.19808456751863793
waypoint29.pose.orientation.w = 0.9801849336278099

# hall/ entrance hall/ foyer / lobby carpet
waypoint30 = PoseStamped()
waypoint30.header.frame_id = 'map'
waypoint30.pose.position.x = 1.2553787231445312
waypoint30.pose.position.y = -11.870269775390625
waypoint30.pose.orientation.z = 0.38118599485622034
waypoint30.pose.orientation.w = 0.9244983706451156

# hall/ entrance hall/ foyer / lobby plant
waypoint31 = PoseStamped()
waypoint31.header.frame_id = 'map'
waypoint31.pose.position.x = -0.8970990180969238
waypoint31.pose.position.y = -14.260936737060547
waypoint31.pose.orientation.z = -0.946649516925858
waypoint31.pose.orientation.w = 0.3222649408546324

# hall/ entrance hall/ foyer / lobby painting
waypoint32 = PoseStamped()
waypoint32.header.frame_id = 'map'
waypoint32.pose.position.x = 1.3281784057617188
waypoint32.pose.position.y = -14.02630615234375
waypoint32.pose.orientation.z = -0.7012621390257386
waypoint32.pose.orientation.w = 0.7129035084561203

# hall/ entrance hall/ foyer / lobby door
waypoint33 = PoseStamped()
waypoint33.header.frame_id = 'map'
waypoint33.pose.position.x = -0.49750471115112305
waypoint33.pose.position.y = -11.767436981201172
waypoint33.pose.orientation.z = -0.9990998584828792
waypoint33.pose.orientation.w = 0.04242019306286738

#####################################################
# laundry room
waypoint34 = PoseStamped()
waypoint34.header.frame_id = 'map'
waypoint34.pose.position.x = 4.449617385864258
waypoint34.pose.position.y = -4.005526065826416
waypoint34.pose.orientation.z = 0.05961125258760106
waypoint34.pose.orientation.w = 0.9982216680502067

# laundry room cat
waypoint35 = PoseStamped()
waypoint35.header.frame_id = 'map'
waypoint35.pose.position.x = 5.9657368659973145
waypoint35.pose.position.y = -3.57163143157959
waypoint35.pose.orientation.z = 0.38935300707913995
waypoint35.pose.orientation.w = 0.9210886145634584

# laundry room washing machine / washer
waypoint36 = PoseStamped()
waypoint36.header.frame_id = 'map'
waypoint36.pose.position.x = 5.724459648132324
waypoint36.pose.position.y = -3.7542929649353027
waypoint36.pose.orientation.z = 0.00611501569987489
waypoint36.pose.orientation.w = 0.9999813031167084

# laundry room cupboard/wardrope/closet
waypoint37 = PoseStamped()
waypoint37.header.frame_id = 'map'
waypoint37.pose.position.x = 5.8009161949157715
waypoint37.pose.position.y = -4.539397716522217
waypoint37.pose.orientation.z = 0.02618751895498612
waypoint37.pose.orientation.w = 0.9996332241456614


##########################################
# center of flat:
waypoint38 = PoseStamped()
waypoint38.header.frame_id = 'map'
waypoint38.pose.position.x = -2.391216278076172
waypoint38.pose.position.y = -0.10757255554199219
waypoint38.pose.orientation.z = 0.02708167616950478
waypoint38.pose.orientation.w = 0.9996332241456614
