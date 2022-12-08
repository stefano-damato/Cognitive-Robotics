// Generated by gencpp from file rasa_ros/RestRequest.msg
// DO NOT EDIT!


#ifndef RASA_ROS_MESSAGE_RESTREQUEST_H
#define RASA_ROS_MESSAGE_RESTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rasa_ros
{
template <class ContainerAllocator>
struct RestRequest_
{
  typedef RestRequest_<ContainerAllocator> Type;

  RestRequest_()
    {
    }
  RestRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::rasa_ros::RestRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rasa_ros::RestRequest_<ContainerAllocator> const> ConstPtr;

}; // struct RestRequest_

typedef ::rasa_ros::RestRequest_<std::allocator<void> > RestRequest;

typedef boost::shared_ptr< ::rasa_ros::RestRequest > RestRequestPtr;
typedef boost::shared_ptr< ::rasa_ros::RestRequest const> RestRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rasa_ros::RestRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rasa_ros::RestRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace rasa_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::RestRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::RestRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::RestRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::RestRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::RestRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::RestRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rasa_ros::RestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::rasa_ros::RestRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::rasa_ros::RestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rasa_ros/RestRequest";
  }

  static const char* value(const ::rasa_ros::RestRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rasa_ros::RestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::rasa_ros::RestRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rasa_ros::RestRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RestRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rasa_ros::RestRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::rasa_ros::RestRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // RASA_ROS_MESSAGE_RESTREQUEST_H