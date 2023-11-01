package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import android.app.AlarmManager;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.os.Build;
import android.content.Context;

import java.util.Timer;
import java.util.TimerTask;

import java.util.Date;
import java.text.SimpleDateFormat;
import java.util.Random;
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 在这里触发函数
                showNotification("Hello");
            }
        });

        Timer timer = new Timer();
        TimerTask task = new TimerTask() {
            @Override
            public void run() {
                // 在这里执行你想要定时调用的函数
                showNotification("Hello");
            }
        };
        timer.schedule(task, 10 * 1000, 10 * 1000);

//        AlarmManager alarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);
//        Intent intent = new Intent(this, YourReceiver.class);
//        PendingIntent pendingIntent = PendingIntent.getBroadcast(this, 0, intent, 0);
// 设置定时任务，使用RTC_WAKEUP确保即使在休眠状态下也能触发
//        alarmManager.setRepeating(AlarmManager.RTC_WAKEUP, System.currentTimeMillis() + initialDelay, period, pendingIntent);
    }

    private String getTimeString() {
        // 获取当前时间
        Date currentTime = new Date();
        // 创建日期格式化器
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        // 格式化当前时间为字符串
        String formattedTime = sdf.format(currentTime);
        return formattedTime;
    }

    private int generateUniqueId() {
        Random random = new Random();
        return random.nextInt(10000); // 使用随机数生成通知ID
    }

    private void showNotification(String message) {
        // 在这里添加弹出通知的代码
        int notificationId = generateUniqueId(); // 通知的唯一标识符
        String channelId = "my_channel_id"; // 通知渠道的ID，可以自定义

//        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, channelId)
//                .setSmallIcon(R.drawable.hello)
//                .setContentTitle("New Message")
//                .setContentText(message)
//                .setAutoCancel(true); // 单击通知后自动取消通知

        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, channelId)
                .setSmallIcon(R.drawable.hello)
                .setContentTitle("New Message")
                .setContentText(message + getTimeString())
                .setPriority(NotificationCompat.PRIORITY_DEFAULT)
                .setAutoCancel(true); // 单击通知后自动取消通知

        // 创建一个意图，当用户点击通知时执行
        Intent resultIntent = new Intent(this, MainActivity.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, resultIntent, PendingIntent.FLAG_IMMUTABLE);
        builder.setContentIntent(pendingIntent);

        // 创建一个通知渠道（仅适用于 Android 8.0 及更高版本）
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            CharSequence channelName = "My Channel"; // 通知渠道的名称
            String channelDescription = "My Channel Description"; // 通知渠道的描述
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel(channelId, channelName, importance);
            channel.setDescription(channelDescription);

            NotificationManager notificationManager = getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }

        // 获取通知管理器
        NotificationManager notificationManager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
//        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);
        // 发送通知
        notificationManager.notify(notificationId, builder.build());
    }
}
