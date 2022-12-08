;; Auto-generated. Do not edit!


(when (boundp 'rasa_ros::ExecuteJS)
  (if (not (find-package "RASA_ROS"))
    (make-package "RASA_ROS"))
  (shadow 'ExecuteJS (find-package "RASA_ROS")))
(unless (find-package "RASA_ROS::EXECUTEJS")
  (make-package "RASA_ROS::EXECUTEJS"))
(unless (find-package "RASA_ROS::EXECUTEJSREQUEST")
  (make-package "RASA_ROS::EXECUTEJSREQUEST"))
(unless (find-package "RASA_ROS::EXECUTEJSRESPONSE")
  (make-package "RASA_ROS::EXECUTEJSRESPONSE"))

(in-package "ROS")





(defclass rasa_ros::ExecuteJSRequest
  :super ros::object
  :slots (_js ))

(defmethod rasa_ros::ExecuteJSRequest
  (:init
   (&key
    ((:js __js) "")
    )
   (send-super :init)
   (setq _js (string __js))
   self)
  (:js
   (&optional __js)
   (if __js (setq _js __js)) _js)
  (:serialization-length
   ()
   (+
    ;; string _js
    4 (length _js)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _js
       (write-long (length _js) s) (princ _js s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _js
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _js (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass rasa_ros::ExecuteJSResponse
  :super ros::object
  :slots (_ack ))

(defmethod rasa_ros::ExecuteJSResponse
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

(defclass rasa_ros::ExecuteJS
  :super ros::object
  :slots ())

(setf (get rasa_ros::ExecuteJS :md5sum-) "0bc1212ef5c5830fe8dbd8060c89a89d")
(setf (get rasa_ros::ExecuteJS :datatype-) "rasa_ros/ExecuteJS")
(setf (get rasa_ros::ExecuteJS :request) rasa_ros::ExecuteJSRequest)
(setf (get rasa_ros::ExecuteJS :response) rasa_ros::ExecuteJSResponse)

(defmethod rasa_ros::ExecuteJSRequest
  (:response () (instance rasa_ros::ExecuteJSResponse :init)))

(setf (get rasa_ros::ExecuteJSRequest :md5sum-) "0bc1212ef5c5830fe8dbd8060c89a89d")
(setf (get rasa_ros::ExecuteJSRequest :datatype-) "rasa_ros/ExecuteJSRequest")
(setf (get rasa_ros::ExecuteJSRequest :definition-)
      "string js
---
string ack
")

(setf (get rasa_ros::ExecuteJSResponse :md5sum-) "0bc1212ef5c5830fe8dbd8060c89a89d")
(setf (get rasa_ros::ExecuteJSResponse :datatype-) "rasa_ros/ExecuteJSResponse")
(setf (get rasa_ros::ExecuteJSResponse :definition-)
      "string js
---
string ack
")



(provide :rasa_ros/ExecuteJS "0bc1212ef5c5830fe8dbd8060c89a89d")


