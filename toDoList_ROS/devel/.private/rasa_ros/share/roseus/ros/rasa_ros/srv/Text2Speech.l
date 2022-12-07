;; Auto-generated. Do not edit!


(when (boundp 'rasa_ros::Text2Speech)
  (if (not (find-package "RASA_ROS"))
    (make-package "RASA_ROS"))
  (shadow 'Text2Speech (find-package "RASA_ROS")))
(unless (find-package "RASA_ROS::TEXT2SPEECH")
  (make-package "RASA_ROS::TEXT2SPEECH"))
(unless (find-package "RASA_ROS::TEXT2SPEECHREQUEST")
  (make-package "RASA_ROS::TEXT2SPEECHREQUEST"))
(unless (find-package "RASA_ROS::TEXT2SPEECHRESPONSE")
  (make-package "RASA_ROS::TEXT2SPEECHRESPONSE"))

(in-package "ROS")





(defclass rasa_ros::Text2SpeechRequest
  :super ros::object
  :slots (_speech ))

(defmethod rasa_ros::Text2SpeechRequest
  (:init
   (&key
    ((:speech __speech) "")
    )
   (send-super :init)
   (setq _speech (string __speech))
   self)
  (:speech
   (&optional __speech)
   (if __speech (setq _speech __speech)) _speech)
  (:serialization-length
   ()
   (+
    ;; string _speech
    4 (length _speech)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _speech
       (write-long (length _speech) s) (princ _speech s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _speech
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _speech (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass rasa_ros::Text2SpeechResponse
  :super ros::object
  :slots (_ack ))

(defmethod rasa_ros::Text2SpeechResponse
  (:init
   (&key
    ((:ack __ack) "")
    )
   (send-super :init)
   (setq _ack (string __ack))
   self)
  (:ack
   (&optional __ack)
   (if __ack (setq _ack __ack)) _ack)
  (:serialization-length
   ()
   (+
    ;; string _ack
    4 (length _ack)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _ack
       (write-long (length _ack) s) (princ _ack s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _ack
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _ack (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass rasa_ros::Text2Speech
  :super ros::object
  :slots ())

(setf (get rasa_ros::Text2Speech :md5sum-) "8be93dfc13258654eb30fdcda5227e42")
(setf (get rasa_ros::Text2Speech :datatype-) "rasa_ros/Text2Speech")
(setf (get rasa_ros::Text2Speech :request) rasa_ros::Text2SpeechRequest)
(setf (get rasa_ros::Text2Speech :response) rasa_ros::Text2SpeechResponse)

(defmethod rasa_ros::Text2SpeechRequest
  (:response () (instance rasa_ros::Text2SpeechResponse :init)))

(setf (get rasa_ros::Text2SpeechRequest :md5sum-) "8be93dfc13258654eb30fdcda5227e42")
(setf (get rasa_ros::Text2SpeechRequest :datatype-) "rasa_ros/Text2SpeechRequest")
(setf (get rasa_ros::Text2SpeechRequest :definition-)
      "string speech
---
string ack
")

(setf (get rasa_ros::Text2SpeechResponse :md5sum-) "8be93dfc13258654eb30fdcda5227e42")
(setf (get rasa_ros::Text2SpeechResponse :datatype-) "rasa_ros/Text2SpeechResponse")
(setf (get rasa_ros::Text2SpeechResponse :definition-)
      "string speech
---
string ack
")



(provide :rasa_ros/Text2Speech "8be93dfc13258654eb30fdcda5227e42")


