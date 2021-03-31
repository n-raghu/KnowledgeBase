while :
do
    echo "Synchronizing..."
    cp /app/src/ /app/public/ /app/tools/ /root/rrals -r

    echo "Resting 5s"
    sleep 5s
done
