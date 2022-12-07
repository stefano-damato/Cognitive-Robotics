;; Auto-generated. Do not edit!


(when (boundp 'rasa_ros::WakeUp)
  (if (not (find-package "RASA_ROS"))
    (make-package "RASA_ROS"))
  (shadow 'WakeUp (find-package "RASA_ROS")))
(unless (find-package "RASA_ROS::WAKEUP")
  (make-package "RASA_ROS::WAKEUP"))
(unless (find-package "RASA_ROS::WAKEUPREQUEST")
  (make-package "RASA_ROS::WAKEUPREQUEST"))
(unless (find-package "RASA_ROS::WAKEUPRESPONSE")
  (make-package "RASA_ROS::WAKEUPRESPONSE"))

(in-package "ROS")





(defclass rasa_ros::WakeUpRequest
  :super ros::object
  :slots ())

(defmethod rasa_ros::WakeUpRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass rasa_ros::WakeUpResponse
  :super ros::object
  :slots (_ack ))

(defmethod rasa_ros::WakeUpResponse
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

(defclass rasa_ros::WakeUp
  :super ros::object
  :slots ())

(setf (get rasa_ros::WakeUp :md5sum-) "b6a73f722475d64a28238118997ef482")
(setf (get rasa_ros::WakeUp :datatype-) "rasa_ros/WakeUp")
(setf (get rasa_ros::WakeUp :request) rasa_ros::WakeUpRequest)
(setf (get rasa_ros::WakeUp :response) rasa_ros::WakeUpResponse)

(defmethod rasa_ros::WakeUpRequest
  (:response () (instance rasa_ros::WakeUpResponse :init)))

(setf (get rasa_ros::WakeUpRequest :md5sum-) "b6a73f722475d64a28238118997ef482")
(setf (get rasa_ros::WakeUpRequest :datatype-) "rasa_ros/WakeUpRequest")
(setf (get rasa_ros::WakeUpRequest :definition-)
      "---
string ack
")

(setf (get rasa_ros::WakeUpResponse :md5sum-) "b6a73f722475d64a28238118997ef482")
(setf (get rasa_ros::WakeUpResponse :datatype-) "rasa_ros/WakeUpResponse")
(setf (get rasa_ros::WakeUpResponse :definition-)
      "---
string ack
")



(provide :rasa_ros/WakeUp "b6a73f722475d64a28238118997ef482")


