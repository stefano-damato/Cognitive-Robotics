// Generated by gencpp from file rasa_ros/Text2Speech.msg
// DO NOT EDIT!


#ifndef RASA_ROS_MESSAGE_TEXT2SPEECH_H
#define RASA_ROS_MESSAGE_TEXT2SPEECH_H

#include <ros/service_traits.h>


#include <rasa_ros/Text2SpeechRequest.h>
#include <rasa_ros/Text2SpeechResponse.h>


namespace rasa_ros
{

struct Text2Speech
{

typedef Text2SpeechRequest Request;
typedef Text2SpeechResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Text2Speech
} // namespace rasa_ros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::rasa_ros::Text2Speech > {
  static const char* value()
  {
    return "8be93dfc13258654eb30fdcda5227e42";
  }

  static const char* value(const ::rasa_ros::Text2Speech&) { return value(); }
};

template<>
struct DataType< ::rasa_ros::Text2Speech > {
  static const char* value()
  {
    return "rasa_ros/Text2Speech";
  }

  static const char* value(const ::rasa_ros::Text2Speech&) { return value(); }
};


// service_traits::MD5Sum< ::rasa_ros::Text2SpeechRequest> should match
// service_traits::MD5Sum< ::rasa_ros::Text2Speech >
template<>
struct MD5Sum< ::rasa_ros::Text2SpeechRequest>
{
  static const char* value()
  {
    return MD5Sum< ::rasa_ros::Text2Speech >::value();
  }
  static const char* value(const ::rasa_ros::Text2SpeechRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::rasa_ros::Text2SpeechRequest> should match
// service_traits::DataType< ::rasa_ros::Text2Speech >
template<>
struct DataType< ::rasa_ros::Text2SpeechRequest>
{
  static const char* value()
  {
    return DataType< ::rasa_ros::Text2Speech >::value();
  }
  static const char* value(const ::rasa_ros::Text2SpeechRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::rasa_ros::Text2SpeechResponse> should match
// service_traits::MD5Sum< ::rasa_ros::Text2Speech >
template<>
struct MD5Sum< ::rasa_ros::Text2SpeechResponse>
{
  static const char* value()
  {
    return MD5Sum< ::rasa_ros::Text2Speech >::value();
  }
  static const char* value(const ::rasa_ros::Text2SpeechResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::rasa_ros::Text2SpeechResponse> should match
// service_traits::DataType< ::rasa_ros::Text2Speech >
template<>
struct DataType< ::rasa_ros::Text2SpeechResponse>
{
  static const char* value()
  {
    return DataType< ::rasa_ros::Text2Speech >::value();
  }
  static const char* value(const ::rasa_ros::Text2SpeechResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // RASA_ROS_MESSAGE_TEXT2SPEECH_H