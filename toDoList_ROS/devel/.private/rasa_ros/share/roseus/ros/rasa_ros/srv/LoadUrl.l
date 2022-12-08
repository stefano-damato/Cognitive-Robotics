;; Auto-generated. Do not edit!


(when (boundp 'rasa_ros::LoadUrl)
  (if (not (find-package "RASA_ROS"))
    (make-package "RASA_ROS"))
  (shadow 'LoadUrl (find-package "RASA_ROS")))
(unless (find-package "RASA_ROS::LOADURL")
  (make-package "RASA_ROS::LOADURL"))
(unless (find-package "RASA_ROS::LOADURLREQUEST")
  (make-package "RASA_ROS::LOADURLREQUEST"))
(unless (find-package "RASA_ROS::LOADURLRESPONSE")
  (make-package "RASA_ROS::LOADURLRESPONSE"))

(in-package "ROS")





(defclass rasa_ros::LoadUrlRequest
  :super ros::object
  :slots (_url ))

(defmethod rasa_ros::LoadUrlRequest
  (:init
   (&key
    ((:url __url) "")
    )
   (send-super :init)
   (setq _url (string __url))
   self)
  (:url
   (&optional __url)
   (if __url (setq _url __url)) _url)
  (:serialization-length
   ()
   (+
    ;; string _url
    4 (length _url)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _url
       (write-long (length _url) s) (princ _url s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _url
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _url (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass rasa_ros::LoadUrlResponse
  :super ros::object
  :slots (_ack ))

(defmethod rasa_ros::LoadUrlResponse
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

(defclass rasa_ros::LoadUrl
  :super ros::object
  :slots ())

(setf (get rasa_ros::LoadUrl :md5sum-) "5562f0f326dc984bc777bae8e1589603")
(setf (get rasa_ros::LoadUrl :datatype-) "rasa_ros/LoadUrl")
(setf (get rasa_ros::LoadUrl :request) rasa_ros::LoadUrlRequest)
(setf (get rasa_ros::LoadUrl :response) rasa_ros::LoadUrlResponse)

(defmethod rasa_ros::LoadUrlRequest
  (:response () (instance rasa_ros::LoadUrlResponse :init)))

(setf (get rasa_ros::LoadUrlRequest :md5sum-) "5562f0f326dc984bc777bae8e1589603")
(setf (get rasa_ros::LoadUrlRequest :datatype-) "rasa_ros/LoadUrlRequest")
(setf (get rasa_ros::LoadUrlRequest :definition-)
      "string url
---
string ack
")

(setf (get rasa_ros::LoadUrlResponse :md5sum-) "5562f0f326dc984bc777bae8e1589603")
(setf (get rasa_ros::LoadUrlResponse :datatype-) "rasa_ros/LoadUrlResponse")
(setf (get rasa_ros::LoadUrlResponse :definition-)
      "string url
---
string ack
")



(provide :rasa_ros/LoadUrl "5562f0f326dc984bc777bae8e1589603")


