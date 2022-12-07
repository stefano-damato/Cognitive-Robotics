;; Auto-generated. Do not edit!


(when (boundp 'rasa_ros::Rest)
  (if (not (find-package "RASA_ROS"))
    (make-package "RASA_ROS"))
  (shadow 'Rest (find-package "RASA_ROS")))
(unless (find-package "RASA_ROS::REST")
  (make-package "RASA_ROS::REST"))
(unless (find-package "RASA_ROS::RESTREQUEST")
  (make-package "RASA_ROS::RESTREQUEST"))
(unless (find-package "RASA_ROS::RESTRESPONSE")
  (make-package "RASA_ROS::RESTRESPONSE"))

(in-package "ROS")





(defclass rasa_ros::RestRequest
  :super ros::object
  :slots ())

(defmethod rasa_ros::RestRequest
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

(defclass rasa_ros::RestResponse
  :super ros::object
  :slots (_ack ))

(defmethod rasa_ros::RestResponse
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

(defclass rasa_ros::Rest
  :super ros::object
  :slots ())

(setf (get rasa_ros::Rest :md5sum-) "b6a73f722475d64a28238118997ef482")
(setf (get rasa_ros::Rest :datatype-) "rasa_ros/Rest")
(setf (get rasa_ros::Rest :request) rasa_ros::RestRequest)
(setf (get rasa_ros::Rest :response) rasa_ros::RestResponse)

(defmethod rasa_ros::RestRequest
  (:response () (instance rasa_ros::RestResponse :init)))

(setf (get rasa_ros::RestRequest :md5sum-) "b6a73f722475d64a28238118997ef482")
(setf (get rasa_ros::RestRequest :datatype-) "rasa_ros/RestRequest")
(setf (get rasa_ros::RestRequest :definition-)
      "---
string ack
")

(setf (get rasa_ros::RestResponse :md5sum-) "b6a73f722475d64a28238118997ef482")
(setf (get rasa_ros::RestResponse :datatype-) "rasa_ros/RestResponse")
(setf (get rasa_ros::RestResponse :definition-)
      "---
string ack
")



(provide :rasa_ros/Rest "b6a73f722475d64a28238118997ef482")


